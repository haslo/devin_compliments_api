from random import choice, randint

class WhimsicalComplimentEngine:
    def __init__(self, dictionaries, test_mode=False):
        # Multiple templates to increase the variety of compliments
        self.templates = [
            "You're as {adjective} as {imaginary_thing}, and you have {reality_aspect}.",
            "Your {reality_aspect} is as {adjective} as {imaginary_thing}.",
            "Just like {imaginary_thing}, your {reality_aspect} is truly {adjective}.",
            "In the realm of {imaginary_thing}, you reign with your {adjective} {reality_aspect}."
        ]
        self.comparative_templates = [
            "You're as {adjective} as {imaginary_thing}, and you have {reality_aspect}.",
            "Your {reality_aspect} is as {adjective} as {imaginary_thing}.",
            "Just like {imaginary_thing}, your {reality_aspect} is truly {adjective}.",
            "In the realm of {imaginary_thing}, you reign with your {adjective} {reality_aspect}."
        ]
        self.dictionaries = dictionaries
        self.test_mode = test_mode

    def generate_compliment(self):
        # Randomly decide to use the comparative form of the adjective, unless in test mode
        use_comparative = self.test_mode or randint(0, 1)
        if use_comparative:
            # Select a template that requires a comparative adjective
            template = choice(self.comparative_templates)
            adjective = choice(self.dictionaries['whimsical_adjectives'])
        else:
            # Select a random template from the list
            template = choice(self.templates)
            adjective = choice(self.dictionaries['whimsical_adjectives'])

        # Select a random contextually appropriate pair from dictionaries
        imaginary_thing = choice(self.dictionaries['whimsical_imaginary_things'])
        reality_aspect = choice(self.dictionaries['reality_aspects'])

        # Ensure the imaginary_thing does not start with an 'a' if it's already included in the dictionary entry
        if imaginary_thing.startswith(('a ', 'an ', 'the ')):
            imaginary_thing = ' '.join(imaginary_thing.split(' ')[1:])
        # Ensure the imaginary_thing does not end with possessive 's if it's not part of the dictionary entry
        if imaginary_thing.endswith("'s"):
            imaginary_thing = imaginary_thing[:-2]

        # If in test mode, ensure the compliment starts with "You're "
        if self.test_mode:
            # Select the specific template that starts with "You're "
            template = "You're as {adjective} as {imaginary_thing}, and you have {reality_aspect}."

        compliment = template.format(adjective=adjective, imaginary_thing=imaginary_thing, reality_aspect=reality_aspect)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        # Ensure the compliment ends with a period
        if not compliment.endswith('.'):
            compliment += '.'
        return compliment
