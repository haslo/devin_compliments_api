from util.dictionary_loader import DictionaryLoader
from random import choice

class InclusiveComplimentEngine:
    def __init__(self):
        self.loader = DictionaryLoader('engines', 'inclusive')
        dictionaries = self.loader.load_dictionary()
        self.templates = dictionaries['inclusive_templates']
        self.adjectives = dictionaries['inclusive_adjectives']
        self.nouns = dictionaries['inclusive_nouns']
        self.activities = dictionaries['inclusive_activities']
        self.admirable_activities = dictionaries['inclusive_admirable_activities']
        self.qualities = dictionaries['inclusive_qualities']  # Corrected key to match the dictionary
        self.verbs = dictionaries['inclusive_verbs']
        self.natural_phenomena = dictionaries['inclusive_natural_phenomena']
        self.person_roles = dictionaries['inclusive_person_roles']

    def generate_compliment(self, template_index=None):
        # Ensure that each attribute category is represented in the generated compliment
        adjective = choice(self.adjectives)
        noun = choice(self.nouns)
        activity = choice(self.activities)
        admirable_activity = choice(self.admirable_activities)
        quality = choice(self.qualities)
        verb = choice(self.verbs)
        natural_phenomenon = choice(self.natural_phenomena)
        person_role = choice(self.person_roles)

        # Select a template based on the provided index or randomly
        template = self.templates[template_index] if template_index is not None else choice(self.templates)
        compliment = template.format(
            adjective=adjective,
            noun=noun,
            activity=activity,
            admirable_activity=admirable_activity,
            quality=quality,
            verb=verb,
            natural_phenomena=natural_phenomenon,
            person_role=person_role
        )

        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        # Ensure the compliment ends with a period
        if not compliment.endswith('.'):
            compliment += '.'

        # Contextual selection of natural phenomena
        # If the template includes natural phenomena, ensure it's contextually positive
        if '{natural_phenomena}' in template:
            positive_phenomena = ['sunrise', 'sunset', 'rainbow', 'aurora', 'blossom']
            if natural_phenomenon not in positive_phenomena:
                # Choose a positive natural phenomenon
                positive_natural_phenomenon = choice(positive_phenomena)
                # Replace only the natural_phenomena placeholder with the positive natural phenomenon
                compliment = compliment.replace('{natural_phenomena}', positive_natural_phenomenon)
                # Re-capitalize the first letter of the compliment in case it changed
                compliment = compliment[0].upper() + compliment[1:]

        return compliment
