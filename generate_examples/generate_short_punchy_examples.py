import sys
sys.path.append('/home/ubuntu/devin_compliments_api')  # Add project directory to Python path

from engines.short_punchy_compliment_engine import ShortPunchyComplimentEngine
from util.dictionary_loader import DictionaryLoader  # Updated import path

# Load dictionaries
dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')  # Adjusted relative path
dictionaries = dictionary_loader.load_dictionaries()

# Create an instance of ShortPunchyComplimentEngine
short_punchy_engine = ShortPunchyComplimentEngine(dictionaries)

# Generate and print 10 short punchy compliments
for _ in range(10):
    print(short_punchy_engine.generate_compliment())
