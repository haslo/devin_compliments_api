from random import choice
from dictionary_loader import DictionaryLoader

class WhimsicalComplimentEngine:
    def __init__(self):
        self.template = "You're {adjective} than {imaginary_thing}, because you're {reality_aspect}."
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def generate_compliment(self):
        # Select a random contextually appropriate triple from dictionaries
        adjective = choice(self.dictionaries['whimsical_adjectives'])
        imaginary_thing = choice(self.dictionaries['whimsical_imaginary_things'])
        reality_aspect = choice(self.dictionaries['whimsical_reality_aspects'])
        compliment = self.template.format(adjective=adjective, imaginary_thing=imaginary_thing, reality_aspect=reality_aspect)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
