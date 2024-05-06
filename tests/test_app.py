import json
import unittest
from app import app
from tests.test_engine_selector import TestEngineSelector
from engines.simple_compliment_engine import SimpleComplimentEngine
from engines.feature_compliment_engine import FeatureComplimentEngine
from engines.elegant_compliment_engine import ElegantComplimentEngine
from engines.direct_praise_compliment_engine import DirectPraiseComplimentEngine

class TestAPIVariety(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        # Instantiate TestEngineSelector without a list of engine classes
        self.engine_selector = TestEngineSelector()

    def test_api_compliment_variety(self):
        # Test to ensure that the API is providing a balanced variety of compliments from each engine
        response = self.app.get('/compliment')
        data = json.loads(response.data)
        compliment = data['compliment']
        # This test needs to be implemented to check for variety
        self.assertTrue(compliment, "Compliment should not be empty.")

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
