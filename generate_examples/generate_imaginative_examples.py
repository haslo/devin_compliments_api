from engines.imaginative_compliment_engine import ImaginativeComplimentEngine
from util.dictionary_loader import DictionaryLoader

# Load dictionaries
# Update the path to the YAML file to be relative to the project root
dictionary_loader = DictionaryLoader('/home/ubuntu/devin_compliments_api/util/compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

# Create an instance of ImaginativeComplimentEngine
engine = ImaginativeComplimentEngine(dictionaries)

# Generate and print a set of example compliments
for _ in range(30):
    print(engine.generate_compliment())
