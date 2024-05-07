import sys
sys.path.append('/home/ubuntu/devin_compliments_api')  # Add project directory to Python path

from engines.inclusive_compliment_engine import InclusiveComplimentEngine
from dictionary_loader import DictionaryLoader  # Corrected import statement

# Load dictionaries
# Update the path to the YAML file to be absolute
dictionary_loader = DictionaryLoader('/home/ubuntu/devin_compliments_api/compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

# Initialize engine
engine = InclusiveComplimentEngine(dictionaries)

# Generate examples
# Update the range to generate 30 examples
for _ in range(30):
    print(engine.generate_compliment())
