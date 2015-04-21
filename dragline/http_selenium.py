from Queue import Queue, Empty
from selenium import webdriver

webdriver.Remote.__len__ = lambda x: 0


class Browser(object):
    def get_driver(self):
        return webdriver.Remote()

    def __init__(self):
        self.browsers = Queue()

    def get_response(self, url, **kwargs):
        try:
            browser = self.browsers.get(block=False)
        except Empty:
            browser = self.get_driver()
        browser.get(url)
        return browser

    def put_response(self, browser):
        self.browsers.put(browser)

    def clear(self):
        while True:
            try:
                browser = self.browsers.get(block=False)
                browser.close()
            except Empty:
                break


class Chrome(Browser):
    def get_driver(self):
        return webdriver.Chrome()


class Firefox(Browser):
    def get_driver(self):
        return webdriver.Firefox()


class PhantomJS(Browser):
    def get_driver(self):
        return webdriver.PhantomJS()
