from random import choice
from util.dictionary_loader import DictionaryLoader

class ShortPunchyComplimentEngine:
    def __init__(self):
        self.loader = DictionaryLoader('engines', 'short_punchy')
        self.dictionaries = self.loader.load_dictionary()
        self.templates = self.dictionaries['short_punchy_templates']
        self.adjectives = self.dictionaries['short_punchy_adjectives']
        self.nouns = self.dictionaries['short_punchy_nouns']

    def generate_compliment(self):
        template = choice(self.templates)
        compliment = template.format(
            adjective=choice(self.adjectives),
            noun=choice(self.nouns)
        )
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        # Ensure the compliment ends with a period
        if not compliment.endswith('.'):
            compliment += '.'
        return compliment
