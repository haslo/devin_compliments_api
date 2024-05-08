import random

class SimpleComplimentEngine:
    def __init__(self, dictionaries):
        self.dictionaries = dictionaries
        self.templates = self.dictionaries['direct_praise_templates']

    def generate_compliment(self):
        # Select a random template from the direct praise templates
        template = random.choice(self.templates)
        # Identify placeholders in the template and select appropriate words
        compliment = template.format(
            positive_adjective=random.choice(self.dictionaries['positive_adjectives']),
            person_role=random.choice(self.dictionaries['person_roles']),
            personal_quality=random.choice(self.dictionaries['personal_qualities']),
            adjective=random.choice(self.dictionaries['adjectives']),
            feature=random.choice(self.dictionaries['features']),
            action=random.choice(self.dictionaries['actions']),
            natural_phenomena=random.choice(self.dictionaries['natural_phenomena']),  # Corrected key to match dictionary
            positive_trait=random.choice(self.dictionaries['positive_traits']),
            celestial_body=random.choice(self.dictionaries['celestial_bodies']),
            positive_thing=random.choice(self.dictionaries['positive_things']),
            shiny_object=random.choice(self.dictionaries['shiny_objects']),
            verb=random.choice(self.dictionaries['verbs'])
        )
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        # Ensure the compliment ends with a period or exclamation mark
        if not (compliment.endswith('.') or compliment.endswith('!')):
            compliment += '.'
        return compliment
