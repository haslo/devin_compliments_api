import sys
sys.path.append('/home/ubuntu/devin_compliments_api')  # Add project directory to Python path

from engines.inclusive_compliment_engine import InclusiveComplimentEngine
from dictionary_loader import DictionaryLoader  # Corrected import statement

# Load dictionaries
dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

# Initialize engine
engine = InclusiveComplimentEngine(dictionaries)

# Generate examples
for _ in range(10):
    print(engine.generate_compliment())
