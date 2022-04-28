from django.test import TestCase
from django.test import SimpleTestCase
from django.test import Client
from django.urls import reverse, resolve


class ViewTestCase(TestCase):
    
    
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('https://127.0.0.1:8080/')
        self.assertEqual(response.status_code, 200)
        
    
    def test_login_page_loads_properly(self):
        """The login page loads properly"""
        response = self.client.get('https://127.0.0.1:8080/accounts/login/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_signup_page_loads_properly(self):
        """The signup page loads properly"""
        response = self.client.get('https://127.0.0.1:8080/accounts/signup/')
        self.assertEqual(response.status_code, 200)