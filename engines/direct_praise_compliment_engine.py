import random

class DirectPraiseComplimentEngine:
    def __init__(self, dictionaries):
        # Multiple templates to increase the variety of compliments
        self.templates = [
            "You are a {adjective} {noun}!",
            "Your {noun} is simply {adjective}!",
            "In a world of {noun}s, you stand out as truly {adjective}.",
            "You embody the very essence of a {adjective} {noun}.",
            "You shine with the {adjective} quality of a {noun}."
        ]
        self.dictionaries = dictionaries

    def generate_compliment(self):
        # Select a random template from the list
        template = random.choice(self.templates)
        adjective = random.choice(self.dictionaries['direct_praise_adjectives'])
        noun = random.choice(self.dictionaries['direct_praise_nouns'])
        compliment = template.format(adjective=adjective, noun=noun)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
