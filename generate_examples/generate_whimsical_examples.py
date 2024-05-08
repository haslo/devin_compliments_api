import sys
sys.path.append('/home/ubuntu/devin_compliments_api')  # Add project directory to Python path

from engines.whimsical_compliment_engine import WhimsicalComplimentEngine
from util.dictionary_loader import DictionaryLoader  # Updated import statement to reflect new util directory

# Load dictionaries
dictionary_loader = DictionaryLoader('/home/ubuntu/devin_compliments_api/util/compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

# Create an instance of WhimsicalComplimentEngine
engine = WhimsicalComplimentEngine(dictionaries)

# Generate and print a set of example compliments
for _ in range(30):
    print(engine.generate_compliment())
