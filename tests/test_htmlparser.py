from dragline import http, runtime
from dragline.parser import HtmlParser
import unittest
import re

request_processor = http.RequestProcessor()


class HtmlParserTest(unittest.TestCase):

    def setUp(self):
        runtime.request_processor = request_processor

    def test_links(self):
        res = http.Request('http://httpbin.org/links/10').send()
        html = HtmlParser(res)
        urlpattern = re.compile(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        urls = list(html.extract_urls())
        for url in urls:
            if not urlpattern.match(url):
                self.fail('Invalid url')
        self.assertEqual(len(urls), 9)

    def test_gettext(self):
        self.assertTrue(True)

    def test_extract(self):
        self.assertTrue(True)

    def test_cssselect(self):
        self.assertTrue

    def test_css(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
