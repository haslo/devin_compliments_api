import unittest
from engines.action_based_compliment_engine import ActionBasedComplimentEngine

class TestActionBasedComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ActionBasedComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertTrue(compliment.startswith("You"))
        self.assertTrue(any(verb in compliment for verb in self.engine.dictionaries['action_based_verbs']))
        self.assertTrue(any(adverb in compliment for adverb in self.engine.dictionaries['action_based_adverbs']))
        self.assertFalse(compliment.endswith("[action_based]."))

if __name__ == '__main__':
    unittest.main()
