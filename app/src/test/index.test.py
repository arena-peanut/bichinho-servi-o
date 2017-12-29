import unittest
from app.src import hello


class IndexTest(unittest.TestCase):
    
    def test_index(self):
        tester = self.app.test_client()
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<h1>hello world</h1>')


if __name__ == '__main__':
    unittest.main()
