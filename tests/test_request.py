import unittest
import os
from dragline.http import Request, RequestError
from requests.compat import urljoin


HTTPBIN = 'http://httpbin.org/'


def httpbin(*suffix):
    """Returns url for HTTPBIN resource."""
    return urljoin(HTTPBIN, '/'.join(suffix))


class RequestTest(unittest.TestCase):

    def test_get(self):
        response = Request(httpbin('get')).send()
        self.assertEqual(httpbin('get'), response.json()['url'])

    def test_post_form(self):
        data = {'name': 'dragline'}
        response = Request(httpbin('post'), form_data=data).send()
        self.assertEqual(data, response.json()['form'])

    def test_post_raw(self):
        data = 'dragline'
        response = Request(httpbin('post'), form_data=data).send()
        self.assertEqual(data, response.json()['data'])

    def test_headers(self):
        headers = {"user-agent": "dragline"}
        response = Request(httpbin('user-agent'), headers=headers).send()
        self.assertEqual(headers, response.json())

    def test_redirect(self):
        response = Request(httpbin('redirect', '4')).send()
        self.assertEqual(httpbin('get'), response.json()['url'])

    #def test_proxy(self):
        #request = Request(httpbin('/ip'), proxy=(ip, port))
        #response = request.send()
        #print response.json()

    def test_cookie(self):
        response = Request(httpbin('cookies', 'set?name=dragline')).send()
        response = Request(httpbin('cookies')).send()
        self.assertEqual(response.json()['cookies']['name'], 'dragline')
        response = Request(httpbin('/cookies/delete?name')).send()
        response = Request(httpbin('cookies'), cookies={'name': 'dragline'}).send()
        self.assertEqual(response.json()['cookies']['name'], 'dragline')

    def test_timeout(self):
        request = Request(httpbin('delay', '3'), timeout=1)
        self.assertRaises(RequestError, request.send)

    def test_unique(self):
        req1 = Request("http://www.google.com", method="POST",
                       form_data={"test1": "abcd", "abcd": "test1"})
        req2 = Request("http://www.google.com", method="POST",
                       form_data={"abcd": "test1", "test1": "abcd"})
        req3 = Request("http://www.google.com", method="POST",
                       form_data={"abcd": "test1", "test1": "abdc"})
        self.assertEqual(req1.get_unique_id(), req2.get_unique_id())
        self.assertNotEqual(req1.get_unique_id(), req3.get_unique_id())


if __name__ == "__main__":
    unittest.main(verbosity=2)
