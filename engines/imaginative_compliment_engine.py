import random

class ImaginativeComplimentEngine:
    def __init__(self, dictionaries):
        self.template = "You're as {comparative} as {imaginary_thing}, and you have {presence}."
        self.dictionaries = dictionaries

    def generate_compliment(self):
        # Select a random contextually appropriate triple from dictionaries
        comparative = random.choice(self.dictionaries['imaginative_comparatives'])
        imaginary_thing = random.choice(self.dictionaries['imaginative_imaginary_things'])
        presence = random.choice(self.dictionaries['imaginative_presences'])

        # Check and remove the leading article from the imaginary_thing if it exists
        articles = ('a ', 'an ', 'the ')
        if imaginary_thing.lower().startswith(articles):
            imaginary_thing = ' '.join(imaginary_thing.split(' ')[1:])

        # Ensure the imaginary_thing does not end with possessive 's if it's not part of the dictionary entry
        if imaginary_thing.endswith("'s"):
            imaginary_thing = imaginary_thing[:-2]

        compliment = self.template.format(comparative=comparative, imaginary_thing=imaginary_thing, presence=presence)
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
