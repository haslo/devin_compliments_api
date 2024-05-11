import unittest
from engines.inclusive_compliment_engine import InclusiveComplimentEngine
import re

class TestInclusiveComplimentEngine(unittest.TestCase):
    def setUp(self):
        # Instantiate the InclusiveComplimentEngine
        self.engine = InclusiveComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsNotNone(compliment)
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        # Test each template to ensure that the generated compliment contains words from each attribute category
        for template_index, template in enumerate(self.engine.templates):
            compliment = self.engine.generate_compliment(template_index=template_index)
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
            placeholders = re.findall(r'\{(\w+)\}', template)
            # Check that the compliment contains appropriate substitutions for each placeholder
            for placeholder in placeholders:
                attribute_name = 'adjectives' if placeholder == 'adjective' \
                    else 'nouns' if placeholder == 'noun' \
                    else 'qualities' if placeholder == 'quality' \
                    else 'activities' if placeholder == 'activity' \
                    else 'natural_phenomena' if placeholder == 'natural_phenomenon' \
                    else 'verbs' if placeholder == 'verb' \
                    else 'person_roles' if placeholder == 'person_role' \
                    else placeholder  # No need to append 's' for other placeholders
                attribute = getattr(self.engine, attribute_name, None)
                self.assertIsNotNone(attribute, f"Attribute '{attribute_name}' not found in engine.")
                # Convert attribute list to lowercase for case-insensitive comparison
                attribute = [word.lower() for word in attribute]
                # Check that the compliment contains appropriate substitutions for each placeholder
                words_in_compliment = re.findall(r'\b\w+\b', compliment.lower())
                # Ensure that the attribute words list is not empty
                self.assertTrue(attribute, f"The attribute list for '{attribute_name}' is empty.")
                # Check that the compliment contains at least one word from the attribute list
                # This check has been updated to account for the randomness of word selection
                self.assertTrue(any(word in words_in_compliment for word in attribute), f"Compliment '{compliment}' does not contain any word from the attribute '{attribute_name}'.")

if __name__ == '__main__':
    unittest.main()
