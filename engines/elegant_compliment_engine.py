from random import choice

class ElegantComplimentEngine:
    def __init__(self, dictionaries):
        self.template = "Your {feature} is as {adjective} as a {noun}, a true {noun2}."
        self.dictionaries = dictionaries

    def generate_compliment(self):
        feature = choice(self.dictionaries['features'])
        adjective = choice(self.dictionaries['elegant_adjectives'])
        noun = choice(self.dictionaries['elegant_nouns'])
        noun2 = choice(self.dictionaries['elegant_nouns'])  # Use the same dictionary for both nouns to avoid 'as' being picked as a noun2
        compliment = self.template.format(feature=feature, adjective=adjective, noun=noun, noun2=noun2)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
