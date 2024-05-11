import sys
import os

import unittest
import string
import re
from engines.simple_compliment_engine import SimpleComplimentEngine
from engines.feature_compliment_engine import FeatureComplimentEngine
from engines.creative_compliment_engine import CreativeComplimentEngine
from engines.imaginative_compliment_engine import ImaginativeComplimentEngine
from engines.inspirational_compliment_engine import InspirationalComplimentEngine
from engines.whimsical_compliment_engine import WhimsicalComplimentEngine
from engines.elegant_compliment_engine import ElegantComplimentEngine
from engines.short_compliment_engine import ShortComplimentEngine
from engines.direct_praise_compliment_engine import DirectPraiseComplimentEngine
from engines.admiration_compliment_engine import AdmirationComplimentEngine
from engines.inclusive_compliment_engine import InclusiveComplimentEngine
from engines.short_punchy_compliment_engine import ShortPunchyComplimentEngine
from util.dictionary_loader import DictionaryLoader
from tests.test_engine_selector import EngineSelectorMock

class TestSimpleComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = SimpleComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Check if the compliment matches one of the direct praise templates
        self.assertTrue(any(compliment.startswith(template.split('{')[0]) for template in self.engine.templates), "Compliment does not match any direct praise templates.")
        # Ensure the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

    def test_template_integrity(self):
        compliment = self.engine.generate_compliment()
        # Check that the placeholders are filled
        self.assertNotIn('{adjective}', compliment, "The placeholder {adjective} is not filled in the compliment")
        self.assertNotIn('{noun}', compliment, "The placeholder {noun} is not filled in the compliment")

class TestFeatureComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = FeatureComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Check that the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

class TestDirectPraiseComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = DirectPraiseComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliments = [self.engine.generate_compliment() for _ in range(10)]
        templates = self.engine.templates
        # Check if compliments match any of the new templates
        self.assertTrue(any(compliment.startswith(template.split('{')[0]) for template in templates for compliment in compliments), "Compliments do not match the new template structures.")
        # Ensure the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(all(compliment[0].isupper() and compliment.endswith('.') for compliment in compliments), "Compliments should start with an uppercase letter and end with a period.")

    def test_new_direct_praise_templates_usage(self):
        compliments = [self.engine.generate_compliment() for _ in range(100)]
        # Check if the new templates are used in the compliments
        # by looking for the presence of words from the engine's attributes that correspond to the placeholders
        verbs_used = any(verb in compliment for verb in self.engine.verbs for compliment in compliments)
        positive_traits_used = any(positive_trait in compliment for positive_trait in self.engine.positive_traits for compliment in compliments)
        positive_adjectives_used = any(positive_adjective in compliment for positive_adjective in self.engine.positive_adjectives for compliment in compliments)
        natural_phenomena_used = any(natural_phenomenon in compliment for natural_phenomenon in self.engine.natural_phenomena for compliment in compliments)
        features_used = any(feature in compliment for feature in self.engine.features for compliment in compliments)

        self.assertTrue(verbs_used, "Verbs from the engine's attributes are not used in the compliments.")
        self.assertTrue(positive_traits_used, "Positive traits from the engine's attributes are not used in the compliments.")
        self.assertTrue(positive_adjectives_used, "Positive adjectives from the engine's attributes are not used in the compliments.")
        self.assertTrue(natural_phenomena_used, "Natural phenomena from the engine's attributes are not used in the compliments.")
        self.assertTrue(features_used, "Features from the engine's attributes are not used in the compliments.")

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
        noun2 = parts[8].strip(string.punctuation)
        self.assertIn(adjective1, self.engine.dictionaries['creative_adjectives'], f"The word {adjective1} is not in the list of creative adjectives.")
        self.assertIn(noun1, self.engine.dictionaries['creative_nouns'], f"The word {noun1} is not in the list of creative nouns.")
        self.assertIn(adjective2, self.engine.dictionaries['creative_adjectives'], f"The word {adjective2} is not in the list of creative adjectives.")
        self.assertIn(noun2, self.engine.dictionaries['creative_nouns'], f"The word {noun2} is not in the list of creative nouns.")
        # Ensure the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")
        self.assertNotEqual(adjective1, adjective2, "The first adjective should not be the same as the second adjective.")
        self.assertNotEqual(noun1, noun2, "The first noun should not be the same as the second noun.")

class TestImaginativeComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ImaginativeComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)
        # Check if the compliment follows the expected imaginative structure
        pattern = r"You're as .+ as .+, and you have .+\."
        self.assertRegex(compliment, pattern, "Compliment does not follow the imaginative structure.")
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

# New test class for AdmirationComplimentEngine
class TestAdmirationComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AdmirationComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the admiration compliment structure is "You radiate {adjective1} energy, it's {adverb} {adjective2}."
        # Check for the presence of adjectives and adverbs in the string
        self.assertTrue(any(entry in compliment for entry in self.engine.adjectives))
        self.assertTrue(any(entry in compliment for entry in self.engine.adverbs))
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

class TestInspirationalComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = InspirationalComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the inspirational compliment structure is "Your {adjective} {noun} {verb} the world."
        # Check for the presence of adjectives, nouns, and verbs in the string
        self.assertTrue(any(entry in compliment for entry in self.engine.dictionaries['inspirational_adjectives']), "Adjectives from the engine's dictionaries are not used in the compliments.")
        self.assertTrue(any(entry in compliment for entry in self.engine.dictionaries['inspirational_nouns']), "Nouns from the engine's dictionaries are not used in the compliments.")
        self.assertTrue(any(entry in compliment for entry in self.engine.dictionaries['inspirational_verbs']), "Verbs from the engine's dictionaries are not used in the compliments.")
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

class TestWhimsicalComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = WhimsicalComplimentEngine()

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Check if the compliment starts with "Your" and ends with a period
        self.assertTrue(compliment.startswith("Your "), "Compliment does not start with 'Your '")
        self.assertTrue(compliment.endswith("."), "Compliment does not end with a period.")
        # Extract the adjective, noun, and verb from the compliment
        parts = compliment[:-1].split()  # Remove the period and split
        adjective = parts[1]  # The word after "Your"
        noun = parts[2]  # The word after the adjective
        verb = parts[-2]  # The second to last word should be the verb
        # Check if the extracted words are in the engine's attributes
        self.assertIn(adjective, self.engine.dictionaries['whimsical_adjectives'], f"The adjective '{adjective}' is not in the list of whimsical adjectives.")
        self.assertIn(noun, self.engine.dictionaries['whimsical_nouns'], f"The noun '{noun}' is not in the list of whimsical nouns.")
        self.assertIn(verb, self.engine.dictionaries['whimsical_verbs'], f"The verb '{verb}' is not in the list of whimsical verbs.")

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    # Function test_presence_of_than_in_compliment removed as it is no longer relevant to the updated template structure

    def test_compliment_structure(self):
        compliments = [self.engine.generate_compliment() for _ in range(100)]
        # Check if compliments match the expected template in test mode
        expected_start = "You're as"
        expected_middle = "and you have"
        self.assertTrue(all(expected_start in compliment and expected_middle in compliment for compliment in compliments), "Compliments do not match the expected template structure.")
        # Check for the usage of both standard and comparative forms of adjectives
        adjectives = self.engine.dictionaries['whimsical_adjectives']
        self.assertTrue(any(adj in compliment for adj in adjectives for compliment in compliments), "Adjectives are not used properly in the compliments.")

    def test_whimsical_compliment_content(self):
        compliment = self.engine.generate_compliment()
        # Split the compliment into parts based on the new template structure
        parts = compliment.split(' and you have ')
        self.assertTrue(parts[0].startswith("You're as "), "Compliment does not start with 'You're as '")
        self.assertTrue(compliment.endswith("."), "Compliment does not end with a period.")
        # Extract the adjective and imaginary thing from the first part
        adjective = parts[0].split()[2]  # The word after "You're as"
        # Extract the full phrase for the imaginary thing
        # The phrase starts after "You're as {adjective} as " and ends at the comma
        start_idx = parts[0].find(adjective) + len(adjective) + 4  # Skip past the adjective and " as "
        end_idx = parts[0].rfind(",")  # The comma after the imaginary thing phrase
        imaginary_thing_phrase = parts[0][start_idx:end_idx].strip()
        # Normalize the extracted phrase for comparison
        normalized_imaginary_thing_phrase = re.sub(r"^(a|an)\s+", "", imaginary_thing_phrase).strip(string.punctuation).lower()
        # Check if the normalized extracted words are in the dictionaries
        self.assertIn(adjective, self.engine.dictionaries['whimsical_adjectives'], f"The adjective '{adjective}' is not in the list of whimsical adjectives.")
        # Check if the full phrase of the imaginary thing is in the list
        # Normalize the list entries for comparison
        normalized_imaginary_things = [re.sub(r"^(a|an)\s+", "", thing).strip(string.punctuation).lower() for thing in self.engine.dictionaries['whimsical_imaginary_things']]
        self.assertIn(normalized_imaginary_thing_phrase, normalized_imaginary_things, f"The imaginary thing phrase '{normalized_imaginary_thing_phrase}' is not in the list of whimsical imaginary things.")
        # Check the reality aspect part
        reality_aspect = parts[1].rstrip('.').strip()
        self.assertIn(reality_aspect, self.engine.dictionaries['reality_aspects'], f"The reality aspect '{reality_aspect}' is not in the list of reality aspects.")

    def test_new_whimsical_adjectives_usage(self):
        compliments = [self.engine.generate_compliment() for _ in range(100)]
        new_whimsical_adjectives = self.engine.dictionaries['whimsical_adjectives']
        # Check if the new whimsical adjectives are used in the compliments
        self.assertTrue(any(adj.lower() in compliment.lower() for adj in new_whimsical_adjectives for compliment in compliments), "None of the new whimsical adjectives are used in the compliments.")

    def test_new_imaginary_things_usage(self):
        compliments = [self.engine.generate_compliment() for _ in range(100)]
        new_imaginary_things = [
            'a griffin\'s majesty', 'an enchanted forest\'s mystery', 'a magic carpet\'s adventure',
            'a philosopher\'s stone\'s wisdom', 'an elixir of life\'s essence'
        ]
        # Check if the new imaginary things are referenced in the compliments
        # The check now accounts for the full phrase of the imaginary things
        self.assertTrue(any(all(word in compliment for word in thing.split()) for thing in new_imaginary_things for compliment in compliments), "None of the new imaginary things are referenced in the compliments.")

class TestElegantComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ElegantComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        # Index of the template with two occurrences of 'as'
        template_index_with_two_as = 2  # This index may need to be adjusted based on the actual position in the list
        compliment = self.engine.generate_compliment(template_index=template_index_with_two_as)
        parts = compliment.split()
        # Find indices of 'as' which is used as a conjunction/preposition, not a noun
        as_indices = [i for i, x in enumerate(parts) if x.lower() == "as"]
        # Ensure there are two occurrences of 'as' for the structure to be valid
        self.assertEqual(len(as_indices), 2, "The compliment should contain two occurrences of 'as'.")
        self.assertTrue(any(entry in compliment for entry in self.engine.adjectives))
        self.assertTrue(any(entry in compliment for entry in self.engine.nouns))
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

class TestShortComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ShortComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)
        self.assertTrue(1 <= len(compliment.split()) <= 6, "Compliment should be short and concise.")

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Split the compliment into parts and remove the engine identifier
        parts = compliment.split()
        # Validate the structure of the compliment
        self.assertIn(parts[0].lower(), [adj.lower() for adj in self.engine.dictionaries['short_adjectives']], f"The adjective '{parts[0].lower()}' is not in the list of short adjectives.")
        self.assertIn(parts[1].strip(string.punctuation).lower(), [noun.lower() for noun in self.engine.dictionaries['short_nouns']], f"The noun '{parts[1].strip(string.punctuation).lower()}' is not in the list of short nouns.")
        self.assertEqual(len(parts), 2, "Compliment should consist of only an adjective and a noun.")
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        # Ensure the compliment ends with a period
        self.assertTrue(compliment.strip().endswith('.'), "Compliment should end with a period.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

class TestInclusiveComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = InclusiveComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        templates = self.engine.templates
        dictionaries = self.engine.loader.load_dictionary()
        for index, template in enumerate(templates):
            compliment = self.engine.generate_compliment(template_index=index)
            template_placeholders = re.findall(r'{(\w+)}', template)
            attributes_present = True
            for placeholder in template_placeholders:
                # Ensure the prefix matches the dictionary keys and pluralize correctly
                attribute_list_name = 'inclusive_' + placeholder
                if placeholder in ['adjective', 'noun', 'verb', 'person_role']:  # Added 'person_role' to the list
                    attribute_list_name += 's'  # Pluralize correctly
                if placeholder == 'quality':
                    attribute_list_name = 'inclusive_qualities'  # Correct pluralization for 'quality'
                if placeholder == 'activity':
                    attribute_list_name = 'inclusive_activities'  # Correct pluralization for 'activity'
                # Check if the engine has an attribute for the constructed list name
                if hasattr(self.engine, attribute_list_name):
                    attribute_list = getattr(self.engine, attribute_list_name)
                    words_in_compliment = [word.lower().rstrip('.').rstrip(',') for word in compliment.split()]
                    attribute_words = [word.lower() for word in attribute_list]
                    # Check if at least one word from the attribute list is in the compliment
                    if not any(word in words_in_compliment for word in attribute_words):
                        attributes_present = False
                        self.fail(f"Compliment '{compliment}' does not contain words from the attribute category '{attribute_list_name}' for template {index}.")
                else:
                    # If the attribute list does not exist as an engine attribute, check if it exists in the dictionary
                    if attribute_list_name not in dictionaries:
                        self.fail(f"Dictionary key '{attribute_list_name}' does not exist in the dictionary. Check the dictionary keys.")
            self.assertTrue(attributes_present, f"Compliment '{compliment}' does not contain words from each attribute category for template {index}.")
            self.assertTrue(compliment[0].isupper() and compliment.endswith('.'), f"Compliment '{compliment}' should start with an uppercase letter and end with a period.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

    def test_inclusivity_of_compliments(self):
        compliment = self.engine.generate_compliment()
        # Check that the compliment does not contain any inappropriate, racist, or sexist language
        # This is a placeholder for the actual implementation of the check
        self.assertTrue(self.is_compliment_inclusive(compliment), "Compliment contains inappropriate content.")

    def is_compliment_inclusive(self, compliment):
        # List of disallowed words or phrases that are considered inappropriate, racist, or sexist
        disallowed_terms = [
            # This list should be populated with actual inappropriate terms
            # For the sake of this example, generic placeholders are used
            'placeholder_inappropriate_term_1',
            'placeholder_inappropriate_term_2',
            'placeholder_racist_term',
            'placeholder_sexist_term',
        ]
        # Check if the compliment contains any of the disallowed terms
        return not any(term.lower() in compliment.lower() for term in disallowed_terms)

class TestShortPunchyComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ShortPunchyComplimentEngine()

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)
        self.assertTrue(1 <= len(compliment.split()) <= 4, "Compliment should be short, consisting of 1 to 4 words.")

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Check that the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")
        # Split the compliment into parts
        parts = compliment.split()
        # Validate the structure of the compliment
        if parts[0].lower() in ['simply', 'truly']:
            # Check if the second part is a noun if the first part is a template word
            noun_phrase = ' '.join(parts[1:]).rstrip('.').lower()
            self.assertTrue(any(noun.lower() in noun_phrase for noun in self.engine.nouns), f"The compliment structure is not valid for template word '{parts[0]}'.")
        elif parts[0].lower() == 'always':
            # Check if the second part is an adjective
            adjective_phrase = ' '.join(parts[1:]).rstrip('.').lower()
            self.assertTrue(any(adjective.lower() in adjective_phrase for adjective in self.engine.adjectives), "The compliment does not contain a valid short punchy adjective.")
        else:
            # Check if the first part is an adjective
            self.assertTrue(any(parts[0].lower() == adjective.lower() for adjective in self.engine.adjectives), "The compliment does not start with a valid short punchy adjective.")
            # Check if the second part is a noun
            if len(parts) > 1:
                noun_phrase = ' '.join(parts[1:]).rstrip('.').lower()
                self.assertTrue(any(noun.lower() in noun_phrase for noun in self.engine.nouns), "The compliment does not contain a valid short punchy noun.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

    def test_inclusivity_of_compliments(self):
        compliment = self.engine.generate_compliment()
        # Check that the compliment does not contain any inappropriate, racist, or sexist language
        self.assertTrue(self.is_compliment_inclusive(compliment), "Compliment contains inappropriate content.")

    def is_compliment_inclusive(self, compliment):
        # List of disallowed words or phrases that are considered inappropriate, racist, or sexist
        disallowed_terms = [
            # This list should be populated with actual inappropriate terms
            # For the sake of this example, generic placeholders are used
            'placeholder_inappropriate_term_1',
            'placeholder_inappropriate_term_2',
            'placeholder_racist_term',
            'placeholder_sexist_term',
        ]
        # Check if the compliment contains any of the disallowed terms
        return not any(term.lower() in compliment.lower() for term in disallowed_terms)

if __name__ == '__main__':
    unittest.main()
