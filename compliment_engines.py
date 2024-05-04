import random
from dictionary_loader import DictionaryLoader

# Load dictionaries from YAML file
dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

class ComplimentEngine:
    def __init__(self, template, components):
        self.template = template
        self.components = components

    def generate_compliment(self):
        compliment = self.template.format(**{k: random.choice(dictionaries[v]) for k, v in self.components.items()})
        return compliment

class SimpleComplimentEngine(ComplimentEngine):
    def __init__(self):
        template = "You're as {adjective} as a {noun}."
        components = {
            'adjective': 'adjectives',
            'noun': 'nouns'
        }
        super().__init__(template, components)

class FeatureComplimentEngine(ComplimentEngine):
    def __init__(self):
        template = "Your {feature} is {compliment}."
        components = {
            'feature': 'features',
            'compliment': 'compliments'
        }
        super().__init__(template, components)

# ... More classes for each compliment engine can be added here
