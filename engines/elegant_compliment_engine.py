from random import choice
from dictionary_loader import DictionaryLoader

class ElegantComplimentEngine:
    def __init__(self):
        self.template = "Your {feature} is as {adjective} as a {noun}, a true {noun2}."
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.id = "elegant"
        # Define contextually appropriate feature-adjective-noun-noun2 quadruples
        self.acceptable_quadruples = [
            ('voice', 'melodic', 'sonnet', 'symphony'),
            ('style', 'elegant', 'painting', 'masterpiece'),
            ('manner', 'graceful', 'dance', 'ballet'),
            # ... more quadruples can be added here
        ]

    def generate_compliment(self):
        # Select a random contextually appropriate quadruple
        feature, adjective, noun, noun2 = choice(self.acceptable_quadruples)
        compliment = self.template.format(feature=feature, adjective=adjective, noun=noun, noun2=noun2)
        return f"{compliment} [{self.id}]."
