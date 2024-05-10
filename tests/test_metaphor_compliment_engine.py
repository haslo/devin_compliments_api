import unittest
from engines.metaphor_compliment_engine import MetaphorComplimentEngine

class TestMetaphorComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = MetaphorComplimentEngine()

    def test_generate_compliment_returns_string(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_generate_compliment_starts_with_template_phrase(self):
        compliment = self.engine.generate_compliment()
        self.assertTrue(compliment.startswith("You are like"))

    def test_generate_compliment_ends_with_period(self):
        compliment = self.engine.generate_compliment()
        self.assertTrue(compliment.strip().endswith("."))

    def test_generate_compliment_contains_metaphor_from_list(self):
        compliment = self.engine.generate_compliment()
        # Extract the metaphor from the compliment, removing the trailing period
        metaphor = compliment[13:].rstrip('.').strip()
        self.assertIn(metaphor, self.engine.metaphors)

    def test_generate_compliment_does_not_contain_placeholder(self):
        compliment = self.engine.generate_compliment()
        self.assertNotIn("{metaphor}", compliment)

if __name__ == '__main__':
    unittest.main()
