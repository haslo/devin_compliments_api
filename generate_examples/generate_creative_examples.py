from engines.creative_compliment_engine import CreativeComplimentEngine
from util.dictionary_loader import DictionaryLoader

# Load dictionaries
dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

# Create an instance of CreativeComplimentEngine
engine = CreativeComplimentEngine(dictionaries)

# Generate and print a set of example compliments
for _ in range(30):
    print(engine.generate_compliment())