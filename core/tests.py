from django.test import TestCase

class ViewTestCase(TestCase):
    
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('https://127.0.0.1:8080/')
        self.assertEqual(response.status_code, 200)
