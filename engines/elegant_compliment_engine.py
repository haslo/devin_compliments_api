from random import choice
from util.dictionary_loader import DictionaryLoader

class ElegantComplimentEngine:
    def __init__(self):
        self.loader = DictionaryLoader('engines', 'elegant')
        self.dictionaries = self.loader.load_dictionary()
        self.adjectives = self.dictionaries['elegant_adjectives']
        self.nouns = self.dictionaries['elegant_nouns']
        self.verbs = self.dictionaries['elegant_verbs']
        self.templates = self.dictionaries['elegant_templates']

    def generate_compliment(self, template_index=None):
        adjective = choice(self.adjectives)
        noun = choice(self.nouns)
        verb = choice(self.verbs)
        # If a specific template index is provided, use that template
        # Otherwise, choose a template randomly
        template = self.templates[template_index] if template_index is not None else choice(self.templates)
        compliment = template.format(adjective=adjective, noun=noun, verb=verb)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
