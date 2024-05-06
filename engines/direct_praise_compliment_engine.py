import random

class DirectPraiseComplimentEngine:
    def __init__(self, dictionaries):
        self.template = "You are a {adjective} {noun}!"
        self.dictionaries = dictionaries

    def generate_compliment(self):
        adjective = random.choice(self.dictionaries['direct_praise_adjectives'])
        noun = random.choice(self.dictionaries['direct_praise_nouns'])
        compliment = self.template.format(adjective=adjective, noun=noun)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
