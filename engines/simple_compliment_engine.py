import random
from dictionary_loader import DictionaryLoader

# Load dictionaries from YAML file
dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

class SimpleComplimentEngine:
    def __init__(self):
        self.template = "You are {adjective} {noun}."
        self.components = {
            'adjective': 'adjectives',
            'noun': 'nouns'
        }
        self.id = "simple"

    def generate_compliment(self):
        # Select a random adjective and noun from the dictionaries
        adjective = random.choice(dictionaries[self.components['adjective']])
        noun = random.choice(dictionaries[self.components['noun']])
        compliment = self.template.format(adjective=adjective, noun=noun)
        return f"{compliment} [{self.id}]"
