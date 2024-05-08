import unittest
from util.dictionary_loader import DictionaryLoader
from engines.inclusive_compliment_engine import InclusiveComplimentEngine

class TestInclusiveComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = InclusiveComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsNotNone(compliment)
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # This is a basic check for the structure of the compliment
        # More robust checks should be added to ensure the compliment
        # adheres to the expected format and uses the correct placeholders
        # Check that the generated compliment does not contain any placeholders
        self.assertNotIn('{', compliment)
        self.assertNotIn('}', compliment)
        # Check that the compliment starts with a capital letter and ends with a period
        self.assertTrue(compliment[0].isupper())
        self.assertTrue(compliment.endswith('.'))

if __name__ == '__main__':
    unittest.main()
