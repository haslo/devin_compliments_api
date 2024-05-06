import unittest
from engines.personal_quality_compliment_engine import PersonalQualityComplimentEngine
from dictionary_loader import DictionaryLoader

class TestPersonalQualityComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = PersonalQualityComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertTrue(compliment.startswith("You are"))
        self.assertTrue(compliment.endswith("!"))

        # Extract the adjective and noun from the compliment
        words = compliment.replace("You are", "").replace("!", "").strip().split(" ")
        adjective = words[0]
        noun = words[1]

        # Check if the adjective and noun are from the specified lists
        self.assertIn(adjective, self.engine.dictionaries['direct_praise_adjectives'])
        self.assertIn(noun, self.engine.dictionaries['direct_praise_nouns'])

if __name__ == '__main__':
    unittest.main()
