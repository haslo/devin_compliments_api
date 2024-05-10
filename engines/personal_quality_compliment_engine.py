import random
from util.dictionary_loader import DictionaryLoader

class PersonalQualityComplimentEngine:
    def __init__(self):
        self.loader = DictionaryLoader('engines', 'personal_quality')
        self.dictionaries = self.loader.load_dictionary()
        # Extract the list of adjectives and nouns from the dictionaries
        self.adjectives = self.dictionaries['personal_quality_adjectives']
        self.nouns = self.dictionaries['personal_quality_nouns']
        self.template = "You are {adjective} {noun}!"

    def generate_compliment(self):
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        compliment = self.template.format(adjective=adjective, noun=noun)
        return compliment
