import unittest
from engines.direct_praise_compliment_engine import DirectPraiseEngine

class TestDirectPraiseEngine(unittest.TestCase):
    def setUp(self):
        self.engine = DirectPraiseEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertTrue(compliment.startswith("You are a"))
        # Adjusted to check that the compliment ends with the engine identifier
        self.assertTrue(compliment.endswith("[direct_praise]."))
        self.assertIn("!", compliment)

        # Check if the adjective and noun are from the specified lists
        words = compliment.replace("You are a", "").replace(" [direct_praise].", "").strip().split(" ")
        # Adjusted to account for the exclamation mark being part of the compliment
        self.assertIn(words[0], self.engine.dictionaries['direct_praise_adjectives'])
        self.assertIn(words[1].replace("!", ""), self.engine.dictionaries['direct_praise_nouns'])

if __name__ == '__main__':
    unittest.main()
