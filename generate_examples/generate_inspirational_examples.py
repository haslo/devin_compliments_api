import sys
sys.path.append('/home/ubuntu/devin_compliments_api')  # Add project directory to Python path

# Updated import statements to use absolute imports
from engines.inspirational_compliment_engine import InspirationalComplimentEngine
from util.dictionary_loader import DictionaryLoader

# Load dictionaries
# Updated the path to use a relative path
dictionary_loader = DictionaryLoader('util/compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

# Create an instance of InspirationalComplimentEngine
engine = InspirationalComplimentEngine(dictionaries)

# Generate and print a set of example compliments
for _ in range(30):
    print(engine.generate_compliment())
