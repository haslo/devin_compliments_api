from random import choice
from dictionary_loader import DictionaryLoader

class ShortComplimentEngine:
    def __init__(self):
        self.template = "{adjective} {noun}."
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def generate_compliment(self):
        adjective = choice(self.dictionaries['adjectives'])
        noun = choice(self.dictionaries['nouns'])
        return self.template.format(adjective=adjective, noun=noun)
