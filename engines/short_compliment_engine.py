from random import choice
from dictionary_loader import DictionaryLoader

class ShortComplimentEngine:
    def __init__(self):
        self.template = "{adjective} {noun}."
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def generate_compliment(self):
        # Select a random contextually appropriate pair from dictionaries
        adjective = choice(self.dictionaries['short_adjectives'])
        noun = choice(self.dictionaries['short_nouns'])
        compliment = self.template.format(adjective=adjective, noun=noun)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
