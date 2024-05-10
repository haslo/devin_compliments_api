import random
from util.dictionary_loader import DictionaryLoader

class FeatureComplimentEngine:
    def __init__(self):
        self.loader = DictionaryLoader('engines', 'feature')
        self.dictionaries = self.loader.load_dictionary()
        # Use feature_templates which include a direct address and a verb
        self.templates = self.dictionaries['templates']

    def generate_compliment(self):
        # Select a random template from the feature templates
        template = random.choice(self.templates)
        # Identify placeholders in the template and select appropriate words
        compliment = template.format(
            noun=self.select_appropriate_word('nouns'),
            adjective=self.select_appropriate_word('adjectives'),
            action=self.select_appropriate_word('actions'),
            positive_adjective=self.select_appropriate_word('positive_adjectives'),
            person_role=self.select_appropriate_word('person_roles'),
            personal_quality=self.select_appropriate_word('personal_qualities'),
            natural_phenomenon=self.select_appropriate_word('natural_phenomena'),
            trait=self.select_appropriate_word('traits'),
            celestial_body=self.select_appropriate_word('celestial_bodies'),
            positive_thing=self.select_appropriate_word('positive_things'),
            shiny_object=self.select_appropriate_word('shiny_objects'),
            verb=self.select_appropriate_word('verbs'),
            singular_noun=self.select_appropriate_word('singular_nouns')
        )
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        # Ensure the compliment ends with a period
        if not compliment.endswith('.'):
            compliment += '.'
        return compliment

    def select_appropriate_word(self, category):
        """
        Selects an appropriate word or phrase from the given category.
        Ensures that the word or phrase fits grammatically into the template.
        """
        if category in self.dictionaries:
            return random.choice(self.dictionaries[category])
        else:
            raise KeyError(f"The category {category} does not exist in the dictionaries.")
