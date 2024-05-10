import random
from util.dictionary_loader import DictionaryLoader

class DirectPraiseComplimentEngine:
    def __init__(self):
        # Initialize the DictionaryLoader with the directory and dictionary name
        self.loader = DictionaryLoader('engines', 'direct_praise')
        # Load the dictionary using the loader
        self.dictionaries = self.loader.load_dictionary()
        # Multiple templates to increase the variety of compliments
        self.templates = [
            "You are a {adjective} {noun}.",
            "Your {noun} is simply {adjective}.",
            "In a world of {noun}s, you stand out as truly {adjective}.",
            "You embody the very essence of a {adjective} {noun}.",
            "You shine with the {adjective} quality of a {noun}.",
            "Every time you {verb}, you showcase your {positive_trait}.",
            "You {verb} like a {positive_adjective} {natural_phenomenon}, {positive_adjective} and {positive_trait}.",
            "Your ability to {verb} is as {positive_adjective} as the {natural_phenomenon} itself.",
            "You are the {positive_trait} in human form, always ready to {verb} and {verb}.",
            "Like a {natural_phenomenon}, your {feature} {verb}s everyone with its {positive_adjective} nature."
        ]
        # Update the keys to match the new YAML file structure
        self.adjectives = self.dictionaries['direct_praise_adjectives']
        self.nouns = self.dictionaries['direct_praise_nouns']
        self.verbs = self.dictionaries['verbs']
        self.positive_traits = self.dictionaries['positive_traits']
        self.positive_adjectives = self.dictionaries['positive_adjectives']
        self.natural_phenomena = self.dictionaries['natural_phenomena']
        self.features = self.dictionaries['features']

    def generate_compliment(self):
        # Select a random template from the list
        template = random.choice(self.templates)
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        # Handle the new templates that include verbs and other placeholders
        if "{verb}" in template:
            verb = random.choice(self.verbs)
            positive_trait = random.choice(self.positive_traits)
            positive_adjective = random.choice(self.positive_adjectives)
            natural_phenomenon = random.choice(self.natural_phenomena)
            feature = random.choice(self.features)
            compliment = template.format(adjective=adjective, noun=noun, verb=verb, positive_trait=positive_trait, positive_adjective=positive_adjective, natural_phenomenon=natural_phenomenon, feature=feature)
        else:
            compliment = template.format(adjective=adjective, noun=noun)
        # Capitalize the first letter of the compliment and ensure it ends with a period
        compliment = compliment[0].upper() + compliment[1:]
        if not compliment.endswith('.'):
            compliment += '.'
        return compliment
