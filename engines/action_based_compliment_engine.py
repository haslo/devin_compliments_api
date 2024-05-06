import random

class ActionBasedComplimentEngine:
    def __init__(self, dictionaries):
        self.template = "You {verb} {adverb}!"
        self.dictionaries = dictionaries

    def generate_compliment(self):
        verb = random.choice(self.dictionaries['action_based_verbs'])
        adverb = random.choice(self.dictionaries['action_based_adverbs'])
        compliment = self.template.format(verb=verb, adverb=adverb)
        return compliment
