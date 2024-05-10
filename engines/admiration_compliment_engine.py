from random import choice
from util.dictionary_loader import DictionaryLoader

class AdmirationComplimentEngine:
    def __init__(self):
        # The dictionary name is hardcoded as the class is specific to the admiration engine
        self.loader = DictionaryLoader('engines', 'admiration')
        # The load_dictionary method is called without the 's' as we are loading a single dictionary
        self.dictionaries = self.loader.load_dictionary()
        self.template = "You radiate {adjective1} energy, it's {adverb} {adjective2}"
        # Update the keys to match the new YAML file structure
        self.adjectives = self.dictionaries['admiration_adjectives']
        self.adverbs = self.dictionaries['admiration_adverbs']

    def generate_compliment(self):
        adjective1 = choice(self.adjectives)
        adjective2 = choice(self.adjectives)
        adverb = choice(self.adverbs)
        return f"{self.template.format(adjective1=adjective1, adverb=adverb, adjective2=adjective2)}."
