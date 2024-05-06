import random
from dictionary_loader import DictionaryLoader

class SimpleComplimentEngine:
    def __init__(self):
        dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = dictionary_loader.load_dictionaries()
        self.templates = self.dictionaries['direct_praise_templates']

    def generate_compliment(self):
        compliment = ""
        attempt_counter = 0
        max_attempts = 10
        # Ensure the compliment includes a person role and a personal quality
        while not any(role in compliment for role in self.dictionaries['person_roles']) or not any(quality in compliment for quality in self.dictionaries['personal_qualities']):
            if attempt_counter >= max_attempts:
                # If max attempts reached, return a default compliment
                return "You are appreciated!"
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
                natural_phenomenon=random.choice(self.dictionaries['natural_phenomena']),
                positive_trait=random.choice(self.dictionaries['positive_traits']),
                celestial_body=random.choice(self.dictionaries['celestial_bodies']),
                positive_thing=random.choice(self.dictionaries['positive_things']),
                shiny_object=random.choice(self.dictionaries['shiny_objects']),
                verb=random.choice(self.dictionaries['verbs'])
            )
            attempt_counter += 1
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
