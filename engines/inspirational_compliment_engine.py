from random import choice
from util.dictionary_loader import DictionaryLoader

class InspirationalComplimentEngine:
    def __init__(self):
        self.loader = DictionaryLoader('engines', 'inspirational')
        self.dictionaries = self.loader.load_dictionary()
        self.template = "Your {adjective} {noun} {verb} the world."

    def generate_compliment(self):
        adjective = choice(self.dictionaries['inspirational_adjectives'])
        noun = choice(self.dictionaries['inspirational_nouns'])
        verb = choice(self.dictionaries['inspirational_verbs'])
        template = choice(self.dictionaries['inspirational_templates'])
        compliment = template.format(adjective=adjective, noun=noun, verb=verb)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return f"{compliment}"
