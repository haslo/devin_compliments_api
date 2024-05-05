import random
from dictionary_loader import DictionaryLoader

class ActionBasedComplimentEngine:
    def __init__(self):
        self.template = "You {verb} {adverb}!"
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def generate_compliment(self):
        verb = random.choice(self.dictionaries['action_based_verbs'])
        adverb = random.choice(self.dictionaries['action_based_adverbs'])
        compliment = self.template.format(verb=verb, adverb=adverb)
        return f"{compliment}."
