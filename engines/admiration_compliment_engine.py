from random import choice
from dictionary_loader import DictionaryLoader

class AdmirationComplimentEngine:
    def __init__(self):
        self.template = "You radiate {adjective1} energy, it's {adverb} {adjective2}."
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def generate_compliment(self):
        adjective1 = choice(self.dictionaries['adjectives'])
        adjective2 = choice(self.dictionaries['adjectives'])
        adverb = 'absolutely'  # This can be changed to a dictionary value if needed in the future
        return self.template.format(adjective1=adjective1, adverb=adverb, adjective2=adjective2)
