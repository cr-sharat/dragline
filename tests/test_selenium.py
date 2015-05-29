#import unittest
#from dragline.http import Request
#from dragline.http.selenium import Firefox
#from dragline import runtime
#from requests.compat import urljoin


#HTTPBIN = 'http://httpbin.org/'
#request_processor = Firefox()


#def httpbin(*suffix):
    #"""Returns url for HTTPBIN resource."""
    #return urljoin(HTTPBIN, '/'.join(suffix))


#class RequestTest(unittest.TestCase):
    #def setUp(self):
        #runtime.request_processor = request_processor
        #self.addCleanup(runtime.request_processor.clear)

    #def test_get(self):
        #runtime.settings.SELENIUM_ARGS['proxy'] = "localhost:3128"
        #response = Request(httpbin('get')).send()
        ##self.assertEqual(httpbin('get'), response.json()['url'])