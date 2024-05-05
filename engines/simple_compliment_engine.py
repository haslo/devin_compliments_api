import random
from dictionary_loader import DictionaryLoader

# Load dictionaries from YAML file
dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

class SimpleComplimentEngine:
    def __init__(self):
        self.template = "You're as {adjective} as a {noun}."
        self.components = {
            'adjective': 'adjectives',
            'noun': 'nouns'
        }

    def generate_compliment(self):
        compliment = self.template.format(**{k: random.choice(dictionaries[v]) for k, v in self.components.items()})
        return compliment
