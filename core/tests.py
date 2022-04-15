from django.test import TestCase

class ViewTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('Djangonetflixclone-env.eba-4zbcam7y.us-west-1.elasticbeanstalk.com')
        self.assertEqual(response.status_code, 200)
