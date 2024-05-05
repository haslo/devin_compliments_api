from random import choice
from dictionary_loader import DictionaryLoader

class WhimsicalComplimentEngine:
    def __init__(self):
        self.template = "You're {adjective} than {imaginary_thing}, because you're {reality_aspect}."
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.id = "whimsical"

    def generate_compliment(self):
        adjective = choice(self.dictionaries['adjectives'])
        imaginary_thing = choice(self.dictionaries['imaginary_things'])
        reality_aspect = choice(self.dictionaries['reality_aspects'])
        return f"{self.template.format(adjective=adjective, imaginary_thing=imaginary_thing, reality_aspect=reality_aspect)} [{self.id}]"
