import unittest
from engines.creative_compliment_engine import CreativeComplimentEngine

class TestCreativeComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = CreativeComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the creative compliment structure is "You have the {adjective} {noun} of a {creative_adjective} {creative_noun}."
        parts = compliment.split()
        # Extract the words from the compliment that correspond to the placeholders
        adjective1 = parts[3]
        noun1 = parts[4]
        adjective2 = parts[7]
        noun2 = parts[8].strip('.')
        self.assertIn(adjective1, self.engine.dictionaries['creative_adjectives'], f"The word {adjective1} is not in the list of creative adjectives.")
        self.assertIn(noun1, self.engine.dictionaries['creative_nouns'], f"The word {noun1} is not in the list of creative nouns.")
        self.assertIn(adjective2, self.engine.dictionaries['creative_adjectives'], f"The word {adjective2} is not in the list of creative adjectives.")
        self.assertIn(noun2, self.engine.dictionaries['creative_nouns'], f"The word {noun2} is not in the list of creative nouns.")
        # Ensure the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")
        self.assertNotEqual(adjective1, adjective2, "The first adjective should not be the same as the second adjective.")
        self.assertNotEqual(noun1, noun2, "The first noun should not be the same as the second noun.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

if __name__ == '__main__':
    unittest.main()
