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
        adjective_phrase = " ".join(words[:-1])  # Join all but the last word to form the adjective phrase
        noun = words[-1]

        # Check if the adjective phrase and noun are from the specified lists
        self.assertTrue(any(adjective_phrase.startswith(adj) for adj in self.engine.adjectives), f"The adjective phrase '{adjective_phrase}' is not found in the list of adjectives.")
        self.assertIn(noun, self.engine.nouns)

if __name__ == '__main__':
    unittest.main()
