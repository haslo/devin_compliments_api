import json
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from util.engine_selector import EngineSelector
from .test_engine_selector import EngineSelectorMock

class TestAPIVariety(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        # Instantiate EngineSelectorMock without a list of engine classes
        self.engine_selector = EngineSelectorMock()
        EngineSelector.instance = self.engine_selector
        # Use dependency injection to replace the default EngineSelector
        self.app.application.testing_engine_selector = self.engine_selector

    def test_api_compliment_variety(self):
        # Call the API multiple times to ensure a variety of compliments
        for _ in range(200):
            response = self.app.get('/compliment')
            self.assertEqual(response.status_code, 200)
        total_usage_count = len(self.engine_selector.engine_usage_count)
        self.assertGreaterEqual(total_usage_count, 10, "Several engines should have been used.")

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
