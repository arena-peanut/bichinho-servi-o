from django.test import Client
import unittest


class ViewTesting(unittest.TestCase):

    def test_view(self):
        c = Client()
        response = c.get('/lost')
        self.assertEquals(response.status_code, 200)

    def test_create_get(self):
        c = Client()
        response = c.get('/lost/create/', {'name': 'juquinha'})
        self.assertEquals(response.status_code, 405)

    def test_create_post(self):
        c = Client()
        response = c.post('/lost/create/', {'name': 'juquinha'})
        self.assertEquals(response.status_code, 200)
