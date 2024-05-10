import unittest
from engines.personal_quality_compliment_engine import PersonalQualityComplimentEngine

class TestPersonalQualityComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = PersonalQualityComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertTrue(compliment.startswith("You are"))
        self.assertTrue(compliment.endswith("!"))

        # Extract the adjective and noun from the compliment
        words = compliment.replace("You are", "").replace("!", "").strip().split(" ")
        adjective = words[0]
        noun = words[1]

        # Check if the adjective and noun are from the specified lists
        self.assertIn(adjective, self.engine.adjectives)
        self.assertIn(noun, self.engine.nouns)

if __name__ == '__main__':
    unittest.main()
