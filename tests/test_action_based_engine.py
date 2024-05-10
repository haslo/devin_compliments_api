import unittest
from engines.action_based_compliment_engine import ActionBasedComplimentEngine
from util.dictionary_loader import DictionaryLoader

class TestActionBasedComplimentEngine(unittest.TestCase):
    def setUp(self):
        # The ActionBasedComplimentEngine does not require a DictionaryLoader instance
        self.engine = ActionBasedComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertTrue(compliment.startswith("You"))
        # Accessing the dictionaries directly from the engine instance
        self.assertTrue(any(word in compliment for word in self.engine.dictionaries['action_based_verbs']))
        self.assertTrue(any(word in compliment for word in self.engine.dictionaries['action_based_adverbs']))
        self.assertFalse(compliment.endswith("[action_based]."))

if __name__ == '__main__':
    unittest.main()
