import unittest
from engines.short_punchy_compliment_engine import ShortPunchyComplimentEngine

class TestShortPunchyComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ShortPunchyComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the short punchy compliment structure is "Such {adjective}, much {noun}."
        parts = compliment.split(', ')
        self.assertEqual(len(parts), 2, "Compliment should have two parts separated by a comma.")
        self.assertTrue(parts[0].startswith('Such '), "The first part of the compliment should start with 'Such'.")
        self.assertTrue(parts[1].startswith('much '), "The second part of the compliment should start with 'much'.")

        # Extract the words from the compliment that correspond to the placeholders
        adjective = parts[0].split()[1]
        noun = parts[1].split()[1].strip('.')
        self.assertIn(adjective, self.engine.adjectives, f"The word {adjective} is not in the list of short punchy adjectives.")
        self.assertIn(noun, self.engine.nouns, f"The word {noun} is not in the list of short punchy nouns.")
        # Ensure the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

if __name__ == '__main__':
    unittest.main()
