import sys
sys.path.append('/home/ubuntu/devin_compliments_api')  # Add project directory to Python path

from engines.feature_compliment_engine import FeatureComplimentEngine
from dictionary_loader import DictionaryLoader  # Corrected import statement

# Load dictionaries
dictionary_loader = DictionaryLoader('/home/ubuntu/devin_compliments_api/compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

# Create an instance of FeatureComplimentEngine
engine = FeatureComplimentEngine(dictionaries)

# Generate and print a set of example compliments
for _ in range(30):
    print(engine.generate_compliment())
