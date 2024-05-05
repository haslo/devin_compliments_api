import random
from dictionary_loader import DictionaryLoader

class FeatureComplimentEngine:
    def __init__(self):
        self.template = "Your {feature} is {adjective}."
        dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = dictionary_loader.load_dictionaries()
        self.acceptable_pairs = self.dictionaries['feature_adjective_pairs']

    def generate_compliment(self):
        # Select a random contextually appropriate pair
        feature, adjective = random.choice(self.acceptable_pairs)
        compliment = self.template.format(feature=feature, adjective=adjective)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
