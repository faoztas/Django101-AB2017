from django.test import TestCase

# Create your tests here.

class MerhabaViewTest(TestCase):
    def test_toplama(self):
        response = self.client.get("/toplama")
        self.assertEqual(response.content, b'30')