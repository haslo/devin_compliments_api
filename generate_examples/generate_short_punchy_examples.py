from engines.short_punchy_compliment_engine import ShortPunchyComplimentEngine
from dictionary_loader import DictionaryLoader

# Load dictionaries
dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

# Create an instance of ShortPunchyComplimentEngine
short_punchy_engine = ShortPunchyComplimentEngine(dictionaries)

# Generate and print 10 short punchy compliments
for _ in range(10):
    print(short_punchy_engine.generate_compliment())
