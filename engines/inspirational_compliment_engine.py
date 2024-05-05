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
        compliment = self.template.format(adjective=adjective, noun=noun, verb=verb)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return f"{compliment}"
