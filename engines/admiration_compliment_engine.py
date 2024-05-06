from random import choice

class AdmirationComplimentEngine:
    def __init__(self, dictionaries):
        self.template = "You radiate {adjective1} energy, it's {adverb} {adjective2}"
        self.dictionaries = dictionaries

    def generate_compliment(self):
        adjective1 = choice(self.dictionaries['adjectives'])
        adjective2 = choice(self.dictionaries['adjectives'])
        adverb = 'absolutely'  # This can be changed to a dictionary value if needed in the future
        return f"{self.template.format(adjective1=adjective1, adverb=adverb, adjective2=adjective2)}."
