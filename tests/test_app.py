import unittest
from app import app

class ComplimentApiTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_compliment_endpoint(self):
        response = self.client.get('/compliment')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        data = response.get_json()
        self.assertIn('compliment', data)
        self.assertIsInstance(data['compliment'], str)

if __name__ == '__main__':
    unittest.main()
