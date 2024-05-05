import json
import unittest
from app import app

class TestAPIVariety(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_api_compliment_variety(self):
        self.assertGreaterEqual(0, 1, f"Test not yet implemented")

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_compliment_endpoint(self):
        response = self.app.get('/compliment')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('compliment', data)
        self.assertIsInstance(data['compliment'], str)

class TestAPIHasResponse(unittest.TestCase):

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
