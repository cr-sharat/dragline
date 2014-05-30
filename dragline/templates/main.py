from dragline.htmlparser import HtmlParser
from dragline.http import Request



class Spider:

    def __init__(self, conf):
        self._name = "$spider_name"
        self._start = Request("http://www.example.org")
        self._allowed_urls_regex = "http://www.example.org"
        self.conf = conf

    def parse(self,response):
        html = HtmlParser(response)
