from random import choice

class InclusiveComplimentEngine:
    def __init__(self, dictionaries):
        self.templates = dictionaries['inclusive_templates']
        self.dictionaries = dictionaries

    def generate_compliment(self):
        template = choice(self.templates)
        compliment = template.format(
            adjective=choice(self.dictionaries['inclusive_adjectives']),
            noun=choice(self.dictionaries['inclusive_nouns']),
            activity=choice(self.dictionaries['inclusive_activities']),
            quality=choice(self.dictionaries['inclusive_qualities'])
        )
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        return compliment
