import unittest
import yaml
from app import app, compliment_templates
from compliment_engines import SimpleComplimentEngine, FeatureComplimentEngine

class ComplimentEngineTestCase(unittest.TestCase):

    def setUp(self):
        self.simple_engine = SimpleComplimentEngine()
        self.feature_engine = FeatureComplimentEngine()

    def test_simple_compliment_engine(self):
        compliment = self.simple_engine.generate_compliment()
        self.assertIsInstance(compliment, str)
        # Check if the generated compliment contains any of the adjectives
        self.assertTrue(any(adj in compliment for adj in self.simple_engine.components['adjective']))
        # Check if the generated compliment contains any of the natural phenomena
        self.assertTrue(any(np in compliment for np in self.simple_engine.components['natural_phenomenon']))

    def test_feature_compliment_engine(self):
        compliment = self.feature_engine.generate_compliment()
        self.assertIsInstance(compliment, str)
        # Check if the generated compliment contains any of the features
        self.assertTrue(any(feature in compliment for feature in self.feature_engine.components['feature']))
        # Check if the generated compliment contains any of the compliments
        self.assertTrue(any(comp in compliment for comp in self.feature_engine.components['compliment']))

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

    def test_compliment_structure(self):
        # Generate a set of compliments to test variety
        compliments = {self.client.get('/compliment').get_json()['compliment'] for _ in range(20)}

        # Check if compliments match any of the templates
        for compliment in compliments:
            self.assertTrue(any(compliment.startswith(template.split('{')[0]) for template in compliment_templates))

    def test_compliment_variety(self):
        # Generate a set of compliments to test variety
        compliments = {self.client.get('/compliment').get_json()['compliment'] for _ in range(20)}

        # Check if at least half of the generated compliments are unique
        self.assertTrue(len(compliments) >= 10)

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
