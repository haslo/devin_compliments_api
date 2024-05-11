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
        # Check if the compliment follows one of the known structures
        if compliment.startswith('Such '):
            # Structure is "Such {adjective}, much {noun}."
            parts = compliment.split(', ')
            self.assertEqual(len(parts), 2, "Compliment should have two parts separated by a comma.")
            self.assertTrue(parts[0].startswith('Such '), "The first part of the compliment should start with 'Such'.")
            self.assertTrue(parts[1].startswith('much '), "The second part of the compliment should start with 'much'.")
            adjective = parts[0].split()[1]
            noun = parts[1].split()[1].rstrip('.')
            # Check for the presence of any dictionary item in the compliment
            self.assertTrue(any(adj in compliment for adj in self.engine.adjectives), f"The compliment does not contain any short punchy adjectives.")
            self.assertTrue(any(n in compliment for n in self.engine.nouns), f"The compliment does not contain any short punchy nouns.")
        else:
            # Structure is "{Template word} {noun}" or "Always {adjective}"
            parts = compliment.split()
            template_word = parts[0]
            # Check if the first word is a template word or an adjective
            if template_word.lower() in ['simply', 'truly', 'always']:
                if template_word.lower() == 'always':
                    # 'Always' is a template word, not an adjective, so the next word should be an adjective
                    self.assertTrue(any(adj in compliment for adj in self.engine.adjectives), f"The compliment does not contain any short punchy adjectives.")
                elif template_word.lower() == 'truly':
                    # If the template word is 'truly', the next word should be a noun
                    self.assertTrue(any(n in compliment for n in self.engine.nouns), f"The compliment does not contain any short punchy nouns.")
                else:
                    # If the template word is 'simply', the next word should be a noun
                    self.assertTrue(any(n in compliment for n in self.engine.nouns), f"The compliment does not contain any short punchy nouns.")
            else:
                # If the compliment does not start with a known template word, the first word should be an adjective
                self.assertTrue(any(adj in compliment for adj in self.engine.adjectives), f"The compliment does not contain any short punchy adjectives.")
        # Ensure the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

if __name__ == '__main__':
    unittest.main()
