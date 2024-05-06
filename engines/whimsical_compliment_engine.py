from random import choice
from dictionary_loader import DictionaryLoader

class WhimsicalComplimentEngine:
    def __init__(self):
        self.template = "You're as {adjective} as {imaginary_thing}."
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def generate_compliment(self):
        # Select a random contextually appropriate pair from dictionaries
        adjective = choice(self.dictionaries['whimsical_adjectives'])
        imaginary_thing = choice(self.dictionaries['whimsical_imaginary_things'])
        compliment = self.template.format(adjective=adjective, imaginary_thing=imaginary_thing)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
