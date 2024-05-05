import random
from dictionary_loader import DictionaryLoader

class DirectPraiseEngine:
    def __init__(self):
        self.template = "You are a {adjective} {noun}!"
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()
        self.id = "direct_praise"

    def generate_compliment(self):
        adjective = random.choice(self.dictionaries['direct_praise_adjectives'])
        noun = random.choice(self.dictionaries['direct_praise_nouns'])
        compliment = self.template.format(adjective=adjective, noun=noun)
        return f"{compliment} [{self.id}]."
