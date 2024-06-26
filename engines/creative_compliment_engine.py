import random

class CreativeComplimentEngine:
    def __init__(self, dictionaries):
        self.template = "You have the {adjective} {noun} of a {creative_adjective} {creative_noun}."
        self.dictionaries = dictionaries

    def generate_compliment(self):
        # Select a random contextually appropriate pair for adjective and noun
        adjective = random.choice(self.dictionaries['creative_adjectives'])
        noun = random.choice(self.dictionaries['creative_nouns'])
        # Select a random contextually appropriate pair for creative_adjective and creative_noun
        creative_adjective = random.choice(self.dictionaries['creative_adjectives'])
        creative_noun = random.choice(self.dictionaries['creative_nouns'])
        compliment = self.template.format(adjective=adjective, noun=noun, creative_adjective=creative_adjective, creative_noun=creative_noun)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
