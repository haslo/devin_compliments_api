import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
from util.dictionary_loader import DictionaryLoader
from .test_engine_selector import EngineSelectorMock

class TestSimpleComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = SimpleComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Check if the compliment matches one of the direct praise templates
        self.assertTrue(any(compliment.startswith(template.split('{')[0]) for template in self.dictionaries['direct_praise_templates']), "Compliment does not match any direct praise templates.")
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
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = FeatureComplimentEngine(self.dictionaries)

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
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = DirectPraiseComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliments = [self.engine.generate_compliment() for _ in range(100)]
        templates = self.engine.templates
        # Check if compliments match any of the new templates
        self.assertTrue(any(any(template.format(adjective=adj, noun=noun) in compliment for adj in self.dictionaries['direct_praise_adjectives'] for noun in self.dictionaries['direct_praise_nouns']) for template in templates for compliment in compliments), "Compliments do not match the new template structures.")
        # Check for the usage of both adjectives and nouns in the compliments
        self.assertTrue(any(adj.lower() in compliment.lower() for adj in self.dictionaries['direct_praise_adjectives'] for compliment in compliments), "Adjectives are not used in the compliments.")
        self.assertTrue(any(noun.lower() in compliment.lower() for noun in self.dictionaries['direct_praise_nouns'] for compliment in compliments), "Nouns are not used in the compliments.")
        # Ensure the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(all(compliment[0].isupper() and compliment.endswith('.') for compliment in compliments), "Compliments should start with an uppercase letter and end with a period.")

    def test_new_direct_praise_templates_usage(self):
        compliments = [self.engine.generate_compliment() for _ in range(100)]
        # Check if the new templates are used in the compliments
        # by looking for the presence of words from the dictionaries that correspond to the placeholders
        verbs_used = any(verb in compliment for verb in self.dictionaries['verbs'] for compliment in compliments)
        positive_traits_used = any(positive_trait in compliment for positive_trait in self.dictionaries['positive_traits'] for compliment in compliments)
        positive_adjectives_used = any(positive_adjective in compliment for positive_adjective in self.dictionaries['positive_adjectives'] for compliment in compliments)
        natural_phenomena_used = any(natural_phenomenon in compliment for natural_phenomenon in self.dictionaries['natural_phenomena'] for compliment in compliments)
        features_used = any(feature in compliment for feature in self.dictionaries['features'] for compliment in compliments)

        self.assertTrue(verbs_used, "Verbs from the dictionary are not used in the compliments.")
        self.assertTrue(positive_traits_used, "Positive traits from the dictionary are not used in the compliments.")
        self.assertTrue(positive_adjectives_used, "Positive adjectives from the dictionary are not used in the compliments.")
        self.assertTrue(natural_phenomena_used, "Natural phenomena from the dictionary are not used in the compliments.")
        self.assertTrue(features_used, "Features from the dictionary are not used in the compliments.")

class TestCreativeComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = CreativeComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the creative compliment structure is "You have the {adjective1} {noun1} of a {adjective2} {noun2}."
        parts = compliment.split()
        # Extract the words from the compliment that correspond to the placeholders
        adjective1 = parts[3]
        noun1 = parts[4]
        adjective2 = parts[7]
        noun2 = parts[8].strip(string.punctuation)
        # Check if the extracted words are in the dictionaries
        self.assertIn(adjective1, self.dictionaries['creative_adjectives'], f"The word {adjective1} is not in the list of creative adjectives.")
        self.assertIn(noun1, self.dictionaries['creative_nouns'], f"The word {noun1} is not in the list of creative nouns.")
        self.assertIn(adjective2, self.dictionaries['creative_adjectives'], f"The word {adjective2} is not in the list of creative adjectives.")
        self.assertIn(noun2, self.dictionaries['creative_nouns'], f"The word {noun2} is not in the list of creative nouns.")
        # Ensure the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")
        # Check that the first adjective and noun are not the same as the second adjective and noun
        self.assertNotEqual(adjective1, adjective2, "The first adjective should not be the same as the second adjective.")
        self.assertNotEqual(noun1, noun2, "The first noun should not be the same as the second noun.")

class TestImaginativeComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = ImaginativeComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)
        self.assertTrue(any(entry in compliment for entry in self.dictionaries['imaginative_presences']), "Compliment does not contain any imaginative presences.")
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

# New test class for AdmirationComplimentEngine
class TestAdmirationComplimentEngine(unittest.TestCase):
    def setUp(self):
        # Assuming AdmirationComplimentEngine is implemented in admiration_compliment_engine.py
        from engines.admiration_compliment_engine import AdmirationComplimentEngine
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = AdmirationComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the admiration compliment structure is "You radiate {adjective1} energy, it's {adverb} {adjective2}."
        # Check for the presence of adjectives and adverbs in the string
        # but since any of those can be multi word, splitting by whitespace would be stupid (but Devin didn't realize)
        self.assertTrue(any(entry in compliment for entry in self.dictionaries['adjectives']))
        self.assertTrue(any(entry in compliment for entry in self.dictionaries['adverbs']))
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

class TestInspirationalComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = InspirationalComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Assuming the inspirational compliment structure is "Your {adjective} {noun} {verb} the world."
        # but since any of those can be multi word, splitting by whitespace would be stupid (but Devin didn't realize)
        self.assertTrue(any(entry in compliment for entry in self.dictionaries['adjectives']))
        self.assertTrue(any(entry in compliment for entry in self.dictionaries['nouns']))
        self.assertTrue(any(entry in compliment for entry in self.dictionaries['verbs']))
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

class TestWhimsicalComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = WhimsicalComplimentEngine(self.dictionaries, test_mode=True)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_presence_of_than_in_compliment(self):
        # This test is no longer needed as the template structure has changed
        # The new template does not include the word 'than'
        pass

    def test_compliment_structure(self):
        compliments = [self.engine.generate_compliment() for _ in range(100)]
        # Check if compliments match the expected template in test mode
        expected_start = "You're as"
        expected_middle = "and you have"
        self.assertTrue(all(expected_start in compliment and expected_middle in compliment for compliment in compliments), "Compliments do not match the expected template structure.")
        # Check for the usage of both standard and comparative forms of adjectives
        adjectives = self.dictionaries['whimsical_adjectives']
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
        self.assertIn(adjective, self.dictionaries['whimsical_adjectives'], f"The adjective '{adjective}' is not in the list of whimsical adjectives.")
        # Check if the full phrase of the imaginary thing is in the list
        # Normalize the list entries for comparison
        normalized_imaginary_things = [re.sub(r"^(a|an)\s+", "", thing).strip(string.punctuation).lower() for thing in self.dictionaries['whimsical_imaginary_things']]
        self.assertIn(normalized_imaginary_thing_phrase, normalized_imaginary_things, f"The imaginary thing phrase '{normalized_imaginary_thing_phrase}' is not in the list of whimsical imaginary things.")
        # Check the reality aspect part
        reality_aspect = parts[1].rstrip('.').strip()
        self.assertIn(reality_aspect, self.dictionaries['reality_aspects'], f"The reality aspect '{reality_aspect}' is not in the list of reality aspects.")

    def test_new_whimsical_adjectives_usage(self):
        compliments = [self.engine.generate_compliment() for _ in range(100)]
        new_whimsical_adjectives = [
            'enchanting', 'quirky', 'mischievous', 'fanciful', 'whimsical', 'spellbinding', 'captivating'
        ]
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
        # The ElegantComplimentEngine class will be implemented in elegant_compliment_engine.py
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = ElegantComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        parts = compliment.split()
        # Find indices of 'as' which is used as a conjunction/preposition, not a noun
        as_indices = [i for i, x in enumerate(parts) if x.lower() == "as"]
        # Ensure there are two occurrences of 'as' for the structure to be valid
        self.assertEqual(len(as_indices), 2, "The compliment should contain two occurrences of 'as'.")
        self.assertTrue(any(entry in compliment for entry in self.dictionaries['elegant_adjectives']))
        self.assertTrue(any(entry in compliment for entry in self.dictionaries['elegant_nouns']))
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

class TestShortComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.engine = ShortComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)
        self.assertTrue(1 <= len(compliment.split()) <= 6, "Compliment should be short and concise.")

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Split the compliment into parts and remove the engine identifier
        parts = compliment.split()
        # Validate the structure of the compliment
        self.assertIn(parts[0].lower(), [adj.lower() for adj in self.dictionaries['short_adjectives']], f"The adjective {parts[0].lower()} is not in the list of short adjectives.")
        self.assertIn(parts[1].strip(string.punctuation).lower(), [noun.lower() for noun in self.dictionaries['short_nouns']], f"The noun {parts[1].strip(string.punctuation).lower()} is not in the list of short nouns.")
        self.assertEqual(len(parts), 2, "Compliment should consist of only an adjective and a noun.")
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        # Ensure the compliment ends with a period
        self.assertTrue(compliment.strip().endswith('.'), "Compliment should end with a period.")

    def test_randomness_of_compliments(self):
        compliments = set(self.engine.generate_compliment() for _ in range(10))
        self.assertTrue(len(compliments) > 1, "Generated compliments should not be all identical")

class TestInclusiveComplimentEngine(unittest.TestCase):
    def setUp(self):
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        # Assuming InclusiveComplimentEngine is implemented in inclusive_compliment_engine.py
        from engines.inclusive_compliment_engine import InclusiveComplimentEngine
        self.engine = InclusiveComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)

    def test_compliment_structure(self):
        compliments = [self.engine.generate_compliment() for _ in range(100)]
        templates = self.engine.templates
        # Check if compliments match any of the new templates
        self.assertTrue(any(any(template.format(adjective=adj, noun=noun, quality=qual, activity=act, verb=vb) in compliment for adj in self.dictionaries['inclusive_adjectives'] for noun in self.dictionaries['inclusive_nouns'] for qual in self.dictionaries['inclusive_qualities'] for act in self.dictionaries['inclusive_activities'] for vb in self.dictionaries['verbs']) for template in templates for compliment in compliments), "Compliments do not match the new inclusive template structures.")
        # Ensure the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(all(compliment[0].isupper() and compliment.endswith('.') for compliment in compliments), "Compliments should start with an uppercase letter and end with a period.")

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
        self.dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        # Assuming ShortPunchyComplimentEngine is implemented in short_punchy_compliment_engine.py
        from engines.short_punchy_compliment_engine import ShortPunchyComplimentEngine
        self.engine = ShortPunchyComplimentEngine(self.dictionaries)

    def test_generate_compliment(self):
        compliment = self.engine.generate_compliment()
        self.assertIsInstance(compliment, str)
        self.assertTrue(1 <= len(compliment.split()) <= 4, "Compliment should be short, consisting of 1 to 4 words.")

    def test_compliment_structure(self):
        compliment = self.engine.generate_compliment()
        # Check that the compliment starts with an uppercase letter and ends with a period
        self.assertTrue(compliment[0].isupper(), "Compliment should start with an uppercase letter.")
        self.assertTrue(compliment.endswith('.'), "Compliment should end with a period.")

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
