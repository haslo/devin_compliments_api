import random
from dictionary_loader import DictionaryLoader

# Load dictionaries from YAML file
dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

class ImaginativeComplimentEngine:
    def __init__(self):
        self.template = "You're {comparative} than {imaginary_thing}, because you're {presence}."
        self.components = {
            'comparative': 'comparatives',
            'imaginary_thing': 'imaginary_things',
            'presence': 'presences'
        }
        self.id = "imaginative"

    def generate_compliment(self):
        compliment = self.template.format(**{k: random.choice(dictionaries[v]) for k, v in self.components.items()})
        return f"{compliment} [{self.id}]"
