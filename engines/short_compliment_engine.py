from util.dictionary_loader import DictionaryLoader
from random import choice

class ShortComplimentEngine:
    def __init__(self):
        # Initialize the DictionaryLoader with the directory and dictionary name
        self.loader = DictionaryLoader('engines', 'short')
        # Load the dictionary using the loader
        self.dictionaries = self.loader.load_dictionary()
        self.template = "{adjective} {noun}."

    def generate_compliment(self):
        # Select a random contextually appropriate pair from dictionaries
        adjective = choice(self.dictionaries['short_adjectives'])
        noun = choice(self.dictionaries['short_nouns'])
        compliment = self.template.format(adjective=adjective, noun=noun)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
