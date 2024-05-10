from random import choice
from util.dictionary_loader import DictionaryLoader

class WhimsicalComplimentEngine:
    def __init__(self, loader=None):
        self.loader = loader if loader else DictionaryLoader('engines', 'whimsical')
        self.dictionaries = self.loader.load_dictionary()
        self.templates = self.dictionaries['whimsical_templates']
        self.adjectives = self.dictionaries['whimsical_adjectives']
        self.nouns = self.dictionaries['whimsical_nouns']
        self.verbs = self.dictionaries['whimsical_verbs']
        self.imaginary_things = self.dictionaries['whimsical_imaginary_things']
        self.reality_aspects = self.dictionaries['reality_aspects']
        self.test_mode = False

    def generate_compliment(self):
        # Select a random adjective, noun, verb, imaginary thing, and reality aspect
        adjective = choice(self.adjectives)
        noun = choice(self.nouns)
        verb = choice(self.verbs)
        imaginary_thing = choice(self.imaginary_things)
        reality_aspect = choice(self.reality_aspects)

        # Construct the compliment using the whimsical template structure
        compliment = f"You're as {adjective} as {imaginary_thing}, and you have {reality_aspect}."
        compliment = compliment[0].upper() + compliment[1:]  # Capitalize the first letter
        if not compliment.endswith('.'):
            compliment += '.'  # Ensure the compliment ends with a period
        return compliment
