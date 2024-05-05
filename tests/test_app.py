import json
import unittest
from app import app
from test_engine_selector import TestEngineSelector
from engines.simple_compliment_engine import SimpleComplimentEngine
from engines.feature_compliment_engine import FeatureComplimentEngine
from engines.creative_compliment_engine import CreativeComplimentEngine
from engines.imaginative_compliment_engine import ImaginativeComplimentEngine
from engines.inspirational_compliment_engine import InspirationalComplimentEngine
from engines.whimsical_compliment_engine import WhimsicalComplimentEngine
from engines.elegant_compliment_engine import ElegantComplimentEngine
from engines.short_compliment_engine import ShortComplimentEngine

class TestAPIVariety(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.engine_selector = TestEngineSelector([
            SimpleComplimentEngine,
            FeatureComplimentEngine,
            CreativeComplimentEngine,
            ImaginativeComplimentEngine,
            InspirationalComplimentEngine,
            WhimsicalComplimentEngine,
            ElegantComplimentEngine,
            ShortComplimentEngine
        ])

    def test_api_compliment_variety(self):
        # Test to ensure that the API is providing a balanced variety of compliments from each engine
        engine_counts = {engine_class.__name__: 0 for engine_class in self.engine_selector.engine_classes}
        for _ in range(100):
            response = self.app.get('/compliment')
            data = json.loads(response.data)
            compliment = data['compliment']
            # Determine which engine would generate the given compliment
            for engine_class in self.engine_selector.engine_classes:
                engine = engine_class()
                if engine.does_compliment_match_structure(compliment):
                    engine_counts[engine_class.__name__] += 1
                    break
        # Check that each engine is used at least once
        for count in engine_counts.values():
            self.assertGreater(count, 0, "Each engine should be used at least once.")

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
