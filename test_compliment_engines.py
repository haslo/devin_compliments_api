import unittest
import string
import json
from engines.simple_compliment_engine import SimpleComplimentEngine
from engines.feature_compliment_engine import FeatureComplimentEngine
from engines.creative_compliment_engine import CreativeComplimentEngine
from engines.imaginative_compliment_engine import ImaginativeComplimentEngine
from engines.inspirational_compliment_engine import InspirationalComplimentEngine
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
        self.assertIn(parts[3].strip(string.punctuation), self.dictionaries['nouns'])

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
        self.assertIn(parts[3].rstrip('.'), self.dictionaries['adjectives'])

class TestCreativeComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = CreativeComplimentEngine()
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the creative compliment structure is "You have the {adjective1} {noun1} of a {adjective2} {noun2}."
        parts = compliment.split()
        self.assertIn(parts[3], self.dictionaries['adjectives'])
        self.assertIn(parts[4], self.dictionaries['nouns'])
        self.assertIn(parts[7], self.dictionaries['adjectives'])
        self.assertIn(parts[8].strip(string.punctuation), self.dictionaries['nouns'])

class TestImaginativeComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ImaginativeComplimentEngine()
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

        # Check if 'because' is in the compliment
        if 'because' in compliment:
            parts = compliment.split('because')
            comparative_part = parts[0].split()
            presence_part = parts[1].split()

            self.assertIn(comparative_part[1], self.dictionaries['comparatives'])
            self.assertIn(comparative_part[3].rstrip(','), self.dictionaries['imaginary_things'])
            self.assertIn(presence_part[1].rstrip('.'), self.dictionaries['presences'])
        else:
            parts = compliment.split()
            self.assertIn(parts[1], self.dictionaries['comparatives'])
            self.assertIn(parts[3].rstrip(','), self.dictionaries['imaginary_things'])
            self.assertIn(parts[5].rstrip('.'), self.dictionaries['presences'])

# New test class for AdmirationComplimentEngine
class TestAdmirationComplimentEngine(unittest.TestCase):
    def setUp(self):
        # Assuming AdmirationComplimentEngine is implemented in admiration_compliment_engine.py
        from engines.admiration_compliment_engine import AdmirationComplimentEngine
        self.engine = AdmirationComplimentEngine()
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the admiration compliment structure is "You radiate {adjective1} energy, it's {adverb} {adjective2}."
        parts = compliment.split()
        # Check for the presence of adjectives in the dictionaries
        self.assertIn(parts[2], self.dictionaries['adjectives'])
        self.assertIn(parts[6].strip(string.punctuation), self.dictionaries['adjectives'])

class TestInspirationalComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = InspirationalComplimentEngine()
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the inspirational compliment structure is "Your {adjective} {noun} {verb} the world."
        parts = compliment.split()
        self.assertIn(parts[1], self.dictionaries['adjectives'])
        self.assertIn(parts[2], self.dictionaries['nouns'])
        self.assertIn(parts[3], self.dictionaries['verbs'])

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
