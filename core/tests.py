from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core import views

class ViewTestCase(TestCase):
    
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('https://127.0.0.1:8080/')
        self.assertEqual(response.status_code, 200)

    def test_profileList_loads_properly(self):
        """The profileList page loads properly"""
        url = reverse("profile_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
# class TestUrls(SimpleTestCase):
    
#     def test_profileList_url_is_resolved(self):
#         url = reverse("profile_list")
#         print(resolve(url))
