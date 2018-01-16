from django.core.serializers import json
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class IndexTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_index(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Page', self.browser.title)

    def test_lost(self):
        self.browser.get('http://localhost:8000/lost/')
        print(self.browser)
        self.assertEquals('name', 'bichinho service')


if __name__ == '__main__':
    unittest.main(warnings='ignore')