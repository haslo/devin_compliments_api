import random
from util.dictionary_loader import DictionaryLoader

class CreativeComplimentEngine:
    def __init__(self):
        self.loader = DictionaryLoader('engines', 'creative')
        self.dictionaries = self.loader.load_dictionary()
        self.template = "You have the {adjective} {noun} of a {creative_adjective} {creative_noun}."

    def generate_compliment(self):
        # Select a random contextually appropriate pair for adjective and noun
        adjective = random.choice(self.dictionaries['creative_adjectives'])
        noun = random.choice(self.dictionaries['creative_nouns'])
        # Ensure the creative_adjective is not the same as the adjective
        creative_adjective = random.choice([word for word in self.dictionaries['creative_adjectives'] if word != adjective])
        # Ensure the creative_noun is not the same as the noun
        creative_noun = random.choice([word for word in self.dictionaries['creative_nouns'] if word != noun])
        compliment = self.template.format(adjective=adjective, noun=noun, creative_adjective=creative_adjective, creative_noun=creative_noun)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
