from random import choice

class ShortPunchyComplimentEngine:
    def __init__(self, dictionaries):
        self.templates = dictionaries['short_punchy_templates']
        self.dictionaries = dictionaries

    def generate_compliment(self):
        template = choice(self.templates)
        compliment = template.format(
            adjective=choice(self.dictionaries['short_punchy_adjectives']),
            noun=choice(self.dictionaries['short_punchy_nouns'])
        )
        # Capitalize the first letter of the compliment
        compliment = compliment[0].upper() + compliment[1:]
        # Ensure the compliment ends with a period
        if not compliment.endswith('.'):
            compliment += '.'
        return compliment
