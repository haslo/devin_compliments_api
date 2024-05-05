import unittest
from engines.superlative_compliment_engine import SuperlativeComplimentEngine

class TestSuperlativeComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = SuperlativeComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertTrue(compliment.startswith("You are"))
        self.assertTrue(compliment.endswith("!"))

        # Extract the adjective and noun from the compliment
        words = compliment.replace("You are", "").replace("!", "").strip().split(" ")
        adjective = words[0]
        noun = words[1]

        # Check if the adjective and noun are from the specified lists
        self.assertIn(adjective, self.engine.dictionaries['short_adjectives'])
        self.assertIn(noun, self.engine.dictionaries['short_nouns'])

if __name__ == '__main__':
    unittest.main()
