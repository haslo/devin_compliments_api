import random

class PersonalQualityComplimentEngine:
    def __init__(self, dictionaries):
        self.template = "You are {adjective} {noun}!"
        self.dictionaries = dictionaries

    def generate_compliment(self):
        adjective = random.choice(self.dictionaries['direct_praise_adjectives'])
        noun = random.choice(self.dictionaries['direct_praise_nouns'])
        compliment = self.template.format(adjective=adjective, noun=noun)
        return compliment
