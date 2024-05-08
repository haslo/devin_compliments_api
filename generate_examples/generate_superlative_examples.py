from engines.superlative_compliment_engine import SuperlativeComplimentEngine
from util.dictionary_loader import DictionaryLoader

# Load dictionaries
dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

# Create an instance of SuperlativeComplimentEngine
engine = SuperlativeComplimentEngine(dictionaries)

# Generate and print a set of example compliments
for _ in range(30):
    print(engine.generate_compliment())
