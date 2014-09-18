from dragline import http
from dragline import htmlparser
import unittest
import data
import re


class HtmlParserTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_links(self):
        res = http.Request('http://httpbin.org/links/10').send()
        html = htmlparser.HtmlParser(res)
        urlpattern = re.compile(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        urls = html.extract_urls()
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
