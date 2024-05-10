import random
from util.dictionary_loader import DictionaryLoader

class SimpleComplimentEngine:
    def __init__(self):
        # Initialize the DictionaryLoader with the directory and dictionary name
        self.loader = DictionaryLoader('engines', 'simple')
        # Load the dictionary internally
        self.dictionaries = self.loader.load_dictionary()
        # Update the keys to match the new YAML file structure
        self.templates = self.dictionaries['simple_templates']
        self.positive_adjectives = self.dictionaries['simple_positive_adjectives']
        self.person_roles = self.dictionaries['simple_person_roles']
        self.personal_qualities = self.dictionaries['simple_personal_qualities']
        # The key 'simple_adjectives' is updated to 'simple_positive_adjectives' to match the YAML file
        self.adjectives = self.dictionaries['simple_positive_adjectives']
        self.features = self.dictionaries['simple_features']
        self.natural_phenomena = self.dictionaries['simple_natural_phenomena']
        self.positive_traits = self.dictionaries['simple_positive_traits']
        self.celestial_bodies = self.dictionaries['simple_celestial_bodies']
        self.positive_things = self.dictionaries['simple_positive_things']
        self.shiny_objects = self.dictionaries['simple_shiny_objects']
        self.verbs = self.dictionaries['simple_verbs']

    def generate_compliment(self):
        # Select a random template from the simple templates
        template = random.choice(self.templates)
        # Identify placeholders in the template and select appropriate words
        compliment = template.format(
            simple_positive_adjective=random.choice(self.positive_adjectives),
            simple_person_role=random.choice(self.person_roles),
            simple_personal_quality=random.choice(self.personal_qualities),
            simple_adjective=random.choice(self.adjectives),
            simple_feature=random.choice(self.features),
            simple_natural_phenomena=random.choice(self.natural_phenomena),
            simple_positive_trait=random.choice(self.positive_traits),
            simple_celestial_body=random.choice(self.celestial_bodies),
            simple_positive_thing=random.choice(self.positive_things),
            simple_shiny_object=random.choice(self.shiny_objects),
            simple_verb=random.choice(self.verbs)
        )
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        # Ensure the compliment ends with a period or exclamation mark
        if not (compliment.endswith('.') or compliment.endswith('!')):
            compliment += '.'
        return compliment
