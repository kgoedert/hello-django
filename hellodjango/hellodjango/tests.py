from django.http import HttpRequest
from django.test import SimpleTestCase


class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_contains_correct_content(self):
        response = self.client.get('/')
        self.assertContains(response, 'hello')
