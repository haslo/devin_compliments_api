import unittest
import string
import json
from engines.simple_compliment_engine import SimpleComplimentEngine
from engines.feature_compliment_engine import FeatureComplimentEngine
from engines.creative_compliment_engine import CreativeComplimentEngine
from engines.imaginative_compliment_engine import ImaginativeComplimentEngine
from engines.inspirational_compliment_engine import InspirationalComplimentEngine
from engines.whimsical_compliment_engine import WhimsicalComplimentEngine
from engines.elegant_compliment_engine import ElegantComplimentEngine
from engines.admiration_compliment_engine import AdmirationComplimentEngine
from engines.short_compliment_engine import ShortComplimentEngine
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
        # Check if the adjective and noun are in the dictionaries
        self.assertIn(parts[2], self.dictionaries['adjectives'], f"The word {parts[2]} is not in the list of adjectives.")
        self.assertIn(parts[3].strip(string.punctuation), self.dictionaries['nouns'], f"The word {parts[3].strip(string.punctuation)} is not in the list of nouns.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

    def test_template_integrity(self):
        compliment = self.engine.generate_compliment()
        # Check that the placeholders are filled
        self.assertNotIn('{adjective}', compliment, "The placeholder {adjective} is not filled in the compliment")
        self.assertNotIn('{noun}', compliment, "The placeholder {noun} is not filled in the compliment")

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
        self.assertIn(parts[1].strip(string.punctuation), self.dictionaries['features'])
        self.assertIn(parts[3].strip(string.punctuation), self.dictionaries['adjectives'])
        # New check for contextually appropriate feature-adjective pairs
        feature_adjective_pair = (parts[1].strip(string.punctuation), parts[3].strip(string.punctuation))
        acceptable_pairs = [
            ('personality', 'amazing'),
            ('sense of humor', 'incredible'),
            ('presence', 'comforting'),
            # ... more pairs can be added here
        ]
        self.assertIn(feature_adjective_pair, acceptable_pairs, f"The pair {feature_adjective_pair} is not contextually appropriate.")
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

    def test_template_integrity(self):
        compliment = self.engine.generate_compliment()
        template = self.engine.template
        placeholders = set(part[1:-1] for part in template.split() if part.startswith('{') and part.endswith('}'))
        for placeholder in placeholders:
            self.assertIn(placeholder, compliment, f"The placeholder {placeholder} is not filled in the compliment")

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
        self.assertIn(parts[6], self.dictionaries['adjectives'])  # Corrected from parts[8] and removed strip punctuation
        self.assertIn(parts[7].strip(string.punctuation), self.dictionaries['nouns'])  # Added strip punctuation
        # New check for contextually appropriate adjective-noun pairs
        adjective1_noun1_pair = (parts[3], parts[4])
        adjective2_noun2_pair = (parts[6], parts[7].strip(string.punctuation))
        acceptable_pairs = [
            ('brilliant', 'mind'),
            ('kind', 'heart'),
            # ... more pairs can be added here
        ]
        self.assertIn(adjective1_noun1_pair, acceptable_pairs, f"The pair {adjective1_noun1_pair} is not contextually appropriate.")
        self.assertIn(adjective2_noun2_pair, acceptable_pairs, f"The pair {adjective2_noun2_pair} is not contextually appropriate.")
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

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
            # Check for 'shooting star' as a single entry in the list of imaginary things
            imaginary_thing = ' '.join(comparative_part[3:5]).rstrip(',')
            self.assertIn(imaginary_thing, self.dictionaries['imaginary_things'])
            presence_part = parts[1].split()
            self.assertIn(presence_part[1].rstrip('.'), self.dictionaries['presences'])
        else:
            parts = compliment.split()
            self.assertIn(parts[1], self.dictionaries['comparatives'])
            # Check for 'shooting star' as a single entry in the list of imaginary things
            imaginary_thing = ' '.join(parts[3:5]).rstrip(',')
            self.assertIn(imaginary_thing, self.dictionaries['imaginary_things'])
            self.assertIn(parts[5].rstrip('.'), self.dictionaries['presences'])
        # New check for contextually appropriate comparative-imaginary_thing pairs
        comparative_imaginary_pair = (parts[1], imaginary_thing)
        acceptable_pairs = [
            ('better', 'unicorn'),
            ('stronger', 'fairy tale'),
            # ... more pairs can be added here
        ]
        self.assertIn(comparative_imaginary_pair, acceptable_pairs, f"The pair {comparative_imaginary_pair} is not contextually appropriate.")
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

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
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

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

class TestWhimsicalComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = WhimsicalComplimentEngine()
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        parts = compliment.split('because')
        first_part = parts[0].split()
        second_part = parts[1].split()
        self.assertIn(first_part[1], self.dictionaries['adjectives'])
        self.assertIn(first_part[3].rstrip(','), self.dictionaries['imaginary_things'])
        self.assertIn(second_part[1].rstrip('.'), self.dictionaries['reality_aspects'])
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

    def test_whimsical_compliment_content(self):
        compliment = self.engine.generate_compliment()
        parts = compliment.split(', because you\'re ')
        self.assertTrue(parts[0].startswith("You're "))
        self.assertTrue(parts[1].endswith("."))
        adjective, imaginary_thing = parts[0][7:].split(' than ')
        reality_aspect = parts[1]
        self.assertIn(adjective, self.dictionaries['adjectives'])
        self.assertIn(imaginary_thing, self.dictionaries['imaginary_things'])
        self.assertIn(reality_aspect.rstrip('.'), self.dictionaries['reality_aspects'])

class TestElegantComplimentEngine(unittest.TestCase):
    def setUp(self):
        # The ElegantComplimentEngine class will be implemented in elegant_compliment_engine.py
        self.engine = ElegantComplimentEngine()
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the elegant compliment structure is "Your {feature} is as {adjective} as a {noun}, a true {noun2}."
        parts = compliment.split()
        self.assertIn(parts[1], self.dictionaries['features'])
        self.assertIn(parts[4], self.dictionaries['adjectives'])
        self.assertIn(parts[7].strip(string.punctuation), self.dictionaries['nouns'])
        self.assertIn(parts[9].strip(string.punctuation), self.dictionaries['nouns'])
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

class TestShortComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ShortComplimentEngine()
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)
        self.assertTrue(1 <= len(compliment.split()) <= 6, "Compliment should be short and concise.")

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        parts = compliment.split()
        self.assertIn(parts[0], self.dictionaries['adjectives'])
        self.assertIn(parts[1].strip(string.punctuation), self.dictionaries['nouns'])
        self.assertEqual(len(parts), 2, "Compliment should consist of only an adjective and a noun.")
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

class TestAPIVariety(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.engines = [SimpleComplimentEngine, FeatureComplimentEngine, CreativeComplimentEngine, ImaginativeComplimentEngine, InspirationalComplimentEngine, WhimsicalComplimentEngine, AdmirationComplimentEngine, ElegantComplimentEngine, ShortComplimentEngine]

    def test_api_compliment_variety(self):
        compliments = [self.app.get('/compliment').data for _ in range(50)]
        engine_output_counts = {engine.__name__: 0 for engine in self.engines}
        for compliment in compliments:
            compliment = compliment.decode('utf-8')
            for engine in self.engines:
                if engine().template in compliment:
                    engine_output_counts[engine.__name__] += 1
        # Check that each engine has generated at least one compliment
        for count in engine_output_counts.values():
            self.assertGreater(count, 0)

if __name__ == '__main__':
    unittest.main()
