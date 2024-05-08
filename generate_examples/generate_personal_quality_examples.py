import sys

# Removed the sys.path.append as it's no longer necessary with absolute imports
from engines.personal_quality_compliment_engine import PersonalQualityComplimentEngine
from util.dictionary_loader import DictionaryLoader  # Updated import statement to reflect new util directory

# Load dictionaries
# Updated the path to use a relative path
dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

# Create an instance of PersonalQualityComplimentEngine
engine = PersonalQualityComplimentEngine(dictionaries)

# Generate and print a set of example compliments
for _ in range(30):
    print(engine.generate_compliment())
