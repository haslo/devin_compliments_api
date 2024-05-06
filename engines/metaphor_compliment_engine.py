import random
from dictionary_loader import DictionaryLoader

# Load dictionaries from YAML file
dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

class MetaphorComplimentEngine:
    def __init__(self):
        self.template = "You are like {metaphor}."
        self.components = {
            'metaphor': 'metaphors'
        }

    def generate_compliment(self):
        # Select a random metaphor from the dictionaries
        metaphor = random.choice(dictionaries[self.components['metaphor']])
        compliment = self.template.format(metaphor=metaphor)
        # Ensure the compliment ends with a period and does not include the engine ID
        return compliment
