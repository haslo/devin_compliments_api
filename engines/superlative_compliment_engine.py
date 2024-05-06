import random

class SuperlativeComplimentEngine:
    def __init__(self, dictionaries):
        self.template = "You are {adjective} {noun}!"
        self.dictionaries = dictionaries

    def generate_compliment(self):
        adjective = random.choice(self.dictionaries['short_adjectives'])
        noun = random.choice(self.dictionaries['short_nouns'])
        compliment = self.template.format(adjective=adjective, noun=noun)
        return compliment
