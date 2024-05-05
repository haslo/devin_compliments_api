from random import choice
from dictionary_loader import DictionaryLoader

class InspirationalComplimentEngine:
    def __init__(self):
        self.template = "Your {adjective} {noun} {verb} the world."
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def generate_compliment(self):
        adjective = choice(self.dictionaries['adjectives'])
        noun = choice(self.dictionaries['nouns'])
        verb = choice(self.dictionaries['verbs'])
        return self.template.format(adjective=adjective, noun=noun, verb=verb)
