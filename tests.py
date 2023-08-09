import unittest
import requests

from linkchecker import _validate_url

s = requests.Session()


class MyFirstTests(unittest.TestCase):

    def test_validate_url_with_broken_link(self):
        not_found_links = []
        not_found_links.append(_validate_url("http://www.brokenlinks23423423423asimai.com"))
        self.assertTrue(not_found_links)

    def test_validate_url_with_valid_link(self):
        not_found_links = []
        not_found_links.append(self._validate_url("http://www.brokenlinks23423423423asimai.com"))
        self.assertTrue(not_found_links)

if __name__ == '__main__':
    unittest.main()