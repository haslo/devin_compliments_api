from random import choice, randint

class WhimsicalComplimentEngine:
    def __init__(self, dictionaries):
        # Multiple templates to increase the variety of compliments
        self.templates = [
            "You're more {adjective} than {imaginary_thing}, because you're {reality_aspect}.",
            "Your {reality_aspect} is as {adjective} as {imaginary_thing}.",
            "Just like {imaginary_thing}, your {reality_aspect} is truly {adjective}.",
            "In the realm of {imaginary_thing}, you reign with your {adjective} {reality_aspect}."
        ]
        self.dictionaries = dictionaries

    def generate_compliment(self):
        # Select a random template from the list
        template = choice(self.templates)
        # Select a random contextually appropriate pair from dictionaries
        adjective = choice(self.dictionaries['whimsical_adjectives'])
        imaginary_thing = choice(self.dictionaries['whimsical_imaginary_things'])
        reality_aspect = choice(self.dictionaries['reality_aspects'])
        # Ensure the imaginary_thing does not start with an 'a' if it's already included in the dictionary entry
        if imaginary_thing.startswith(('a ', 'an ', 'the ')):
            imaginary_thing = ' '.join(imaginary_thing.split(' ')[1:])
        # Ensure the imaginary_thing does not end with possessive 's if it's not part of the dictionary entry
        if imaginary_thing.endswith("'s"):
            imaginary_thing = imaginary_thing[:-2]
        # Randomly decide to use the comparative form of the adjective
        if randint(0, 1):
            adjective = f"more {adjective}"
        compliment = template.format(adjective=adjective, imaginary_thing=imaginary_thing, reality_aspect=reality_aspect)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
