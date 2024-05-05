import unittest
import yaml
from app import app
from engines.simple_compliment_engine import SimpleComplimentEngine
from engines.feature_compliment_engine import FeatureComplimentEngine
from engines.imaginative_compliment_engine import ImaginativeComplimentEngine

class ComplimentEngineTestCase(unittest.TestCase):

    def setUp(self):
        self.simple_engine = SimpleComplimentEngine()
        self.feature_engine = FeatureComplimentEngine()
        self.imaginative_engine = ImaginativeComplimentEngine()

    def test_simple_compliment_engine(self):
        compliment = self.simple_engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_feature_compliment_engine(self):
        compliment = self.feature_engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_imaginative_compliment_engine(self):
        compliment = self.imaginative_engine.generate_compliment()
        self.assertIsInstance(compliment, str)

class ComplimentAPITestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_compliment_endpoint(self):
        response = self.client.get('/compliment')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertIn('compliment', data)
        self.assertIsInstance(data['compliment'], str)

class ComplimentDictionaryLoaderTestCase(unittest.TestCase):
    def setUp(self):
        with open('compliment_dictionaries.yaml', 'r') as file:
            self.dictionaries = yaml.safe_load(file)

    def test_initialization(self):
        self.assertIsNotNone(self.dictionaries)

    def test_yaml_loading(self):
        self.assertIn('adjectives', self.dictionaries)
        self.assertIn('imaginary_things', self.dictionaries)
        self.assertIn('reality_aspects', self.dictionaries)

    def test_yaml_content(self):
        self.assertIn('better', self.dictionaries['adjectives'])
        self.assertIn('unicorn', self.dictionaries['imaginary_things'])
        self.assertIn('real', self.dictionaries['reality_aspects'])

    def test_error_handling_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            with open('nonexistent.yaml', 'r') as file:
                yaml.safe_load(file)

    def test_error_handling_incorrect_format(self):
        with self.assertRaises(yaml.YAMLError):
            yaml.safe_load("unstructured: text, without: proper, yaml: format")

if __name__ == '__main__':
    unittest.main()
