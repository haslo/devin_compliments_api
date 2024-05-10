from util.dictionary_loader import DictionaryLoader
import random

class SuperlativeComplimentEngine:
    def __init__(self):
        self.loader = DictionaryLoader('engines', 'superlative')
        self.dictionaries = self.loader.load_dictionary()
        # Extract the list of adjectives and nouns from the dictionaries
        self.adjectives = self.dictionaries['superlative_adjectives']
        self.nouns = self.dictionaries['superlative_nouns']
        self.template = "You are {adjective} {noun}!"

    def generate_compliment(self):
        # Select a random adjective and noun from the lists
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        compliment = self.template.format(adjective=adjective, noun=noun)
        return compliment
