import random

class FeatureComplimentEngine:
    def __init__(self, dictionaries):
        self.dictionaries = dictionaries
        # Use action_templates which include a direct address and a verb
        self.templates = self.dictionaries['action_templates']

    def generate_compliment(self):
        # Select a random template from the action templates
        template = random.choice(self.templates)
        # Identify placeholders in the template and select appropriate words
        compliment = template.format(
            feature=self.select_appropriate_word('features'),
            adjective=self.select_appropriate_word('adjectives'),
            action=self.select_appropriate_word('actions'),
            positive_adjective=self.select_appropriate_word('positive_adjectives'),
            person_role=self.select_appropriate_word('person_roles'),
            personal_quality=self.select_appropriate_word('personal_qualities'),
            natural_phenomenon=self.select_appropriate_word('natural_phenomena'),
            positive_trait=self.select_appropriate_word('positive_traits'),
            celestial_body=self.select_appropriate_word('celestial_bodies'),
            positive_thing=self.select_appropriate_word('positive_things'),
            shiny_object=self.select_appropriate_word('shiny_objects'),
            verb=self.select_appropriate_word('verbs'),
            noun=self.select_appropriate_word('singular_nouns')  # Added noun placeholder handling
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
        if category in ['features', 'person_roles', 'personal_qualities', 'positive_traits', 'celestial_bodies', 'positive_things', 'shiny_objects', 'singular_nouns']:  # Added 'singular_nouns' to the list
            # These categories should be used as nouns in the template
            word = random.choice(self.dictionaries[category])
            # Ensure that the word is preceded by an appropriate article if necessary
            if word in self.dictionaries['singular_nouns']:
                # Check if the word starts with a vowel sound for correct article usage, considering case insensitivity
                if word[0].lower() in 'aeiou':
                    word = 'an ' + word
                else:
                    word = 'a ' + word
            return word
        elif category in ['adjectives', 'positive_adjectives']:
            # These categories should be used as adjectives in the template
            word = random.choice(self.dictionaries[category])
            # Ensure that the adjective is not used redundantly
            if word in ['more', 'most']:
                # Select another word that is not a comparative or superlative
                word = random.choice([w for w in self.dictionaries[category] if w not in ['more', 'most']])
            return word
        elif category == 'verbs':
            # These categories should be used as verbs in the template
            verb = random.choice(self.dictionaries[category])
            # Ensure that the verb is in the correct tense
            if ' ' in verb:
                # If the verb phrase is more than one word, ensure it starts with a verb in the correct tense
                verb = 'to ' + verb
            return verb
        elif category == 'actions':
            # These categories should be used as action phrases in the template
            action_phrase = random.choice(self.dictionaries[category])
            # Ensure that the action phrase fits grammatically
            if ' ' in action_phrase:
                # If the action phrase is more than one word, ensure it starts with a verb
                action_phrase = 'to ' + action_phrase
            return action_phrase
        else:
            # For all other categories, return a random choice
            return random.choice(self.dictionaries[category])
