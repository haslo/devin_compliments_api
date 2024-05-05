import random
from dictionary_loader import DictionaryLoader

# Load dictionaries from YAML file
dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

class FeatureComplimentEngine:
    def __init__(self):
        self.template = "Your {feature} is {adjective}."
        self.components = {
            'feature': 'features',
            'adjective': 'adjectives'
        }
        self.id = "feature"
        # Define contextually appropriate feature-adjective pairs
        self.acceptable_pairs = [
            ('smile', 'radiant'),
            ('style', 'impeccable'),
            ('sense of humor', 'infectious'),
            # ... more pairs can be added here
        ]

    def generate_compliment(self):
        # Select a random contextually appropriate pair
        feature, adjective = random.choice(self.acceptable_pairs)
        compliment = self.template.format(feature=feature, adjective=adjective)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return f"{compliment} [{self.id}]."
