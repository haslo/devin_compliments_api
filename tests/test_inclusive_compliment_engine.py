import unittest
from engines.inclusive_compliment_engine import InclusiveComplimentEngine
import re

class TestInclusiveComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = InclusiveComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsNotNone(compliment)
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # This is a basic check for the structure of the compliment
        # More robust checks should be added to ensure the compliment
        # adheres to the expected format and uses the correct placeholders
        # Check that the generated compliment does not contain any placeholders
        self.assertNotIn('{', compliment)
        self.assertNotIn('}', compliment)
        # Check that the compliment starts with a capital letter and ends with a period
        self.assertTrue(compliment[0].isupper())
        self.assertTrue(compliment.endswith('.'))
        # Extract placeholders from the template
        template = self.engine.templates[0]  # Using the first template for testing
        placeholders = re.findall(r'\{(\w+)\}', template)
        # Check that the compliment contains appropriate substitutions for each placeholder
        for placeholder in placeholders:
            attribute = getattr(self.engine, placeholder + 's', None)
            self.assertIsNotNone(attribute, f"Attribute {placeholder + 's'} not found in engine.")
            # Convert attribute list to lowercase for case-insensitive comparison
            attribute = [word.lower() for word in attribute]
            # Check that at least one word from the attribute list is in the compliment
            words_in_compliment = [word.lower() for word in compliment.split()]
            # Ensure that the attribute words list is not empty
            self.assertTrue(attribute, f"The attribute list for {placeholder + 's'} is empty.")
            # Check that at least one word from the attribute list is in the compliment
            self.assertTrue(any(word in words_in_compliment for word in attribute), f"Compliment '{compliment}' does not contain any word from the attribute {placeholder + 's'}.")

if __name__ == '__main__':
    unittest.main()
