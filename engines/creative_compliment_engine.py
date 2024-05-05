import random
from dictionary_loader import DictionaryLoader

# Load dictionaries from YAML file
dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

class CreativeComplimentEngine:
    def __init__(self):
        self.template = "You have the {adjective1} {noun1} of a {adjective2} {noun2}."
        self.components = {
            'adjective1': 'adjectives',
            'noun1': 'nouns',
            'adjective2': 'adjectives',
            'noun2': 'nouns'
        }
        self.id = "creative"

    def generate_compliment(self):
        compliment = self.template.format(**{k: random.choice(dictionaries[v]) for k, v in self.components.items()})
        return f"{compliment} [{self.id}]"
