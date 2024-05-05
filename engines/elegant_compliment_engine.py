from random import choice
from dictionary_loader import DictionaryLoader

class ElegantComplimentEngine:
    def __init__(self):
        self.template = "Your {feature} is as {adjective} as a {noun}, a true {noun2}."
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def generate_compliment(self):
        feature = choice(self.dictionaries['features'])
        adjective = choice(self.dictionaries['adjectives'])
        noun = choice(self.dictionaries['nouns'])
        noun2 = choice(self.dictionaries['nouns'])
        return self.template.format(feature=feature, adjective=adjective, noun=noun, noun2=noun2)
