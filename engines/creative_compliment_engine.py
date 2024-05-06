import random
from dictionary_loader import DictionaryLoader

class CreativeComplimentEngine:
    def __init__(self):
        self.template = "You have the {adjective1} {noun1} of a {adjective2} {noun2}."
        self.dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
        self.dictionaries = self.dictionary_loader.load_dictionaries()

    def generate_compliment(self):
        # Select a random contextually appropriate pair for adjective1 and noun1
        adjective1 = random.choice(self.dictionaries['creative_adjectives'])
        noun1 = random.choice(self.dictionaries['creative_nouns'])
        # Select a random contextually appropriate pair for adjective2 and noun2
        adjective2 = random.choice(self.dictionaries['creative_adjectives'])
        noun2 = random.choice(self.dictionaries['creative_nouns'])
        compliment = self.template.format(adjective1=adjective1, noun1=noun1, adjective2=adjective2, noun2=noun2)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
