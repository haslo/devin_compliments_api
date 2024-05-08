import unittest
from ..engines.action_based_compliment_engine import ActionBasedComplimentEngine

class TestActionBasedComplimentEngine(unittest.TestCase):
    def setUp(self):
        # Mock dictionaries for testing
        self.mock_dictionaries = {
            'action_based_verbs': ['shine', 'inspire', 'create'],
            'action_based_adverbs': ['brightly', 'powerfully', 'creatively']
        }
        self.engine = ActionBasedComplimentEngine(self.mock_dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertTrue(compliment.startswith("You"))
        self.assertTrue(any(verb in compliment for verb in self.mock_dictionaries['action_based_verbs']))
        self.assertTrue(any(adverb in compliment for adverb in self.mock_dictionaries['action_based_adverbs']))
        self.assertFalse(compliment.endswith("[action_based]."))

if __name__ == '__main__':
    unittest.main()
