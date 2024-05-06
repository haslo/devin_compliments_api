import random

class MetaphorComplimentEngine:
    def __init__(self, dictionaries):
        self.template = "You are like {metaphor}."
        self.dictionaries = dictionaries

    def generate_compliment(self):
        # Select a random metaphor from the dictionaries
        metaphor = random.choice(self.dictionaries['metaphors'])
        compliment = self.template.format(metaphor=metaphor)
        # Ensure the compliment ends with a period and does not include the engine ID
        return compliment
