import time
import json
import re
import logging

import redisds
from request import Request, RequestError


class Crawl:

    def __init__(self, spider, settings):
        self.url_set = redisds.Set('urlset', spider._name,)
        self.url_queue = redisds.Queue('urlqueue', spider._name, json)
        self.running_count = redisds.Counter("count", namespace=spider._name)
        self.allowed_urls_regex = re.compile(spider._allowed_urls_regex)
        self.spider = spider
        self.settings = settings

    def start(self, resume, request):
        if not resume and self.count() == 0:
            self.url_queue.clear()
            self.url_set.clear()
        if request.callback is None:
            request.callback = "parse"
        self.insert(request)

    def count(self):
        return self.running_count.get()

    def inc_count(self):
        self.running_count.inc()

    def decr_count(self):
        self.running_count.decr()

    def insert(self, request, check=True):
        if not isinstance(request, Request):
            return
        reqhash = request.get_unique_id()
        if check:
            if not self.allowed_urls_regex.match(request.url):
                return
            elif reqhash in self.url_set:
                return
        self.url_set.add(reqhash)
        self.url_queue.put(request.__dict__)


class Crawler:

    @classmethod
    def load_spider(Crawler, module, resume, settings):
        Crawler.crawl = Crawl(module, settings)
        Crawler.crawl.start(resume, module._start)

    def process_url(self):
        retry = 0
        crawl = Crawler.crawl
        logger = logging.getLogger("dragline")
        settings = crawl.settings
        while True:
            if not retry:
                request = crawl.url_queue.get(timeout=2)
            if request:
                request = Request(**request)
                logger.info("Processing %s", request)
                crawl.inc_count()
                try:
                    response, content = request.send()
                    try:
                        callback = getattr(crawl.spider, request.callback)
                        if request.meta:
                            requests = callback(response, content, request.meta)
                        else:
                            requests = callback(response, content)
                    except:
                        logging.exception("Failed to execute callback")
                        requests = None
                    if requests:
                        for i in requests:
                            crawl.insert(i)
                except RequestError as e:
                    request.retry = request.retry + 1
                    if retry == settings.MAX_RETRY:
                        logger.warning("Rejecting %s", request.url)
                    else:
                        crawl.insert(request, False)
                except Exception as e:
                    logger.exception('Failed to open the url %s', request.url)
                else:
                    logger.info("Finished processing %s", request)
                finally:
                    crawl.decr_count()
            else:
                if crawl.count() == 0:
                    break
                logger.debug("Waiting for %s", crawl.count())
