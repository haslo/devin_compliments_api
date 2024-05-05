import random
from dictionary_loader import DictionaryLoader

class SimpleComplimentEngine:
    def __init__(self):
        self.template = "You are {adjective} {noun}."
        dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = dictionary_loader.load_dictionaries()

    def generate_compliment(self):
        # Select a random adjective and noun from the dictionaries
        adjective = random.choice(self.dictionaries['adjectives'])
        noun = random.choice(self.dictionaries['nouns'])
        compliment = self.template.format(adjective=adjective, noun=noun)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
