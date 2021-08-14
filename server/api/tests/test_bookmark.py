import json

from rest_framework.test import APITestCase
from rest_framework import status


class BookMarkTest(APITestCase):

    fixtures = ['test_data.json']

    def setUp(self):
        self.client.post('/api/bookmark/', {'bookMarkID': 1})

    def test_get_bookmarks(self):
        response = self.client.get('/api/bookmark/')
        json_content = json.loads(response.content)
        self.assertEqual(json_content[0]['id'], 1)

    def test_post_invalid_string_bookMarkID(self):
        data = {
            'bookMarkID': "abc",
        }
        response = self.client.post('/api/bookmark/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.client.session.get("bookMarkIDs"), [1])

    def test_post_invalid_none_bookMarkID(self):
        data = {}
        response = self.client.post('/api/bookmark/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.client.session.get("bookMarkIDs"), [1])

    def test_post_valid_bookMarkID(self):
        data = {
            'bookMarkID': "2",
        }
        response = self.client.post('/api/bookmark/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.client.session.get("bookMarkIDs"), [1, 2])