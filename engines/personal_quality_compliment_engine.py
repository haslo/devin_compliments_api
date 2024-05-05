import random
from dictionary_loader import DictionaryLoader

class PersonalQualityComplimentEngine:
    def __init__(self):
        self.template = "You are {adjective} {noun}!"
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def generate_compliment(self):
        adjective = random.choice(self.dictionaries['direct_praise_adjectives'])
        noun = random.choice(self.dictionaries['direct_praise_nouns'])
        compliment = self.template.format(adjective=adjective, noun=noun)
        return compliment
