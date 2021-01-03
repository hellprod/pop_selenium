import requests
import json
import jsonpath
import unittest

# url_base = "http://localhost:9999/"
# url_all = "api/rest/v1/certificates/all"


class MyTestCase(unittest.TestCase):
    def __init__(self):
        # super().__init__()
        self.url_base = "http://localhost:9999/"
        self.url_all = "api/rest/v1/certificates/all"

    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_show_all_certificates_GET200(self):
        url = self.url_base+self.url_base

        response = requests.get(url)
        assert response.status_code == 200


    # def test_nazwa(self):
    #     print('sad')


if __name__ == '__main__':
    unittest.main()
