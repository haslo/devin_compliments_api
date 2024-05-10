from util.dictionary_loader import DictionaryLoader
import random

class MetaphorComplimentEngine:
    def __init__(self):
        # Initialize the DictionaryLoader with the directory and dictionary name
        self.loader = DictionaryLoader('engines', 'metaphor')
        # Load the dictionary using the loader
        self.dictionaries = self.loader.load_dictionary()
        # Extract the list of metaphors from the dictionaries
        self.metaphors = self.dictionaries['metaphor_metaphors']
        self.template = "You are like {metaphor}."

    def generate_compliment(self):
        # Select a random metaphor from the list of metaphors
        metaphor = random.choice(self.metaphors)
        compliment = self.template.format(metaphor=metaphor)
        # Ensure the compliment ends with a period and does not include the engine ID
        return compliment
