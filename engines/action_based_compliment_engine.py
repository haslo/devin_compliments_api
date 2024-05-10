from util.dictionary_loader import DictionaryLoader
import random

class ActionBasedComplimentEngine:
    def __init__(self):
        self.loader = DictionaryLoader('engines', 'action_based')
        self.dictionaries = self.loader.load_dictionary()
        self.template = "You {verb} {adverb}!"

    def generate_compliment(self):
        verb = random.choice(self.dictionaries['action_based_verbs'])
        adverb = random.choice(self.dictionaries['action_based_adverbs'])
        compliment = self.template.format(verb=verb, adverb=adverb)
        return compliment
