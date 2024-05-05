import unittest
from flask import json
from engines.simple_compliment_engine import SimpleComplimentEngine
from engines.feature_compliment_engine import FeatureComplimentEngine
from dictionary_loader import DictionaryLoader
from app import app

class TestSimpleComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = SimpleComplimentEngine()
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        parts = compliment.split()
        # Assuming the simple compliment structure is "You are {adjective} {noun}."
        self.assertIn(parts[2], self.dictionaries['adjectives'])
        self.assertIn(parts[3], self.dictionaries['nouns'])

class TestFeatureComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = FeatureComplimentEngine()
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the feature compliment structure is "Your {feature} is {adjective}."
        parts = compliment.split()
        self.assertIn(parts[1], self.dictionaries['features'])
        self.assertIn(parts[3], self.dictionaries['adjectives'])

    def test_compliment_appropriateness(self):
        compliments = [self.engine.generate_compliment() for _ in range(100)]
        for compliment in compliments:
            self.assertNotIn(compliment, self.dictionaries['inappropriate_phrases'])

# New test case for a third engine
class TestCreativeComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = CreativeComplimentEngine()  # This class will be created next
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the creative compliment structure is "You have the {adjective} {noun} of a {adjective} {noun}."
        parts = compliment.split()
        self.assertIn(parts[3], self.dictionaries['adjectives'])
        self.assertIn(parts[4], self.dictionaries['nouns'])
        self.assertIn(parts[7], self.dictionaries['adjectives'])
        self.assertIn(parts[8], self.dictionaries['nouns'])

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_compliment_endpoint(self):
        response = self.app.get('/compliment')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('compliment', data)
        self.assertIsInstance(data['compliment'], str)

if __name__ == '__main__':
    unittest.main()
