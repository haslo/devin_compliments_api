import random
import yaml
# Update the import paths to reflect the new 'util' directory
from util.dictionary_loader import DictionaryLoader
from engines.direct_praise_compliment_engine import DirectPraiseComplimentEngine
from engines.whimsical_compliment_engine import WhimsicalComplimentEngine
from engines.feature_compliment_engine import FeatureComplimentEngine
from engines.inspirational_compliment_engine import InspirationalComplimentEngine
from engines.personal_quality_compliment_engine import PersonalQualityComplimentEngine
from engines.whimsical_compliment_engine import WhimsicalComplimentEngine
from engines.metaphor_compliment_engine import MetaphorComplimentEngine
from engines.admiration_compliment_engine import AdmirationComplimentEngine
from engines.imaginative_compliment_engine import ImaginativeComplimentEngine
from engines.simple_compliment_engine import SimpleComplimentEngine
from engines.short_punchy_compliment_engine import ShortPunchyComplimentEngine
from engines.inclusive_compliment_engine import InclusiveComplimentEngine
from engines.action_based_compliment_engine import ActionBasedComplimentEngine
from engines.creative_compliment_engine import CreativeComplimentEngine
from engines.direct_praise_compliment_engine import DirectPraiseComplimentEngine
from engines.short_compliment_engine import ShortComplimentEngine
from engines.elegant_compliment_engine import ElegantComplimentEngine
from engines.superlative_compliment_engine import SuperlativeComplimentEngine

# Instantiate the dictionary loader with the new path to 'compliment_dictionaries.yaml'
dictionary_loader = DictionaryLoader('../util/compliment_dictionaries.yaml')
# Load the dictionaries using the dictionary loader
dictionaries = dictionary_loader.load_dictionaries()

# Instantiate the compliment engine classes with the loaded dictionaries
direct_praise_engine = DirectPraiseComplimentEngine(dictionaries)
whimsical_engine = WhimsicalComplimentEngine(dictionaries)
feature_engine = FeatureComplimentEngine(dictionaries)
inspirational_engine = InspirationalComplimentEngine(dictionaries)
personal_quality_engine = PersonalQualityComplimentEngine(dictionaries)
metaphor_engine = MetaphorComplimentEngine(dictionaries)
admiration_engine = AdmirationComplimentEngine(dictionaries)
imaginative_engine = ImaginativeComplimentEngine(dictionaries)
simple_engine = SimpleComplimentEngine(dictionaries)
short_punchy_engine = ShortPunchyComplimentEngine(dictionaries)
inclusive_engine = InclusiveComplimentEngine(dictionaries)
action_based_engine = ActionBasedComplimentEngine(dictionaries)
creative_engine = CreativeComplimentEngine(dictionaries)
direct_praise_engine = DirectPraiseComplimentEngine(dictionaries)
short_engine = ShortComplimentEngine(dictionaries)
elegant_engine = ElegantComplimentEngine(dictionaries)
superlative_engine = SuperlativeComplimentEngine(dictionaries)

# Create a set to store unique compliments
unique_compliments = set()

# Define the number of iterations for generating compliments
iterations = 1000000  # Adjust the number as needed to estimate uniqueness

# Loop to generate compliments and add to the set
for _ in range(iterations):
    unique_compliments.add(direct_praise_engine.generate_compliment())
    unique_compliments.add(whimsical_engine.generate_compliment())
    unique_compliments.add(feature_engine.generate_compliment())
    unique_compliments.add(inspirational_engine.generate_compliment())
    unique_compliments.add(personal_quality_engine.generate_compliment())
    unique_compliments.add(metaphor_engine.generate_compliment())
    unique_compliments.add(admiration_engine.generate_compliment())
    unique_compliments.add(imaginative_engine.generate_compliment())
    unique_compliments.add(simple_engine.generate_compliment())
    unique_compliments.add(short_punchy_engine.generate_compliment())
    unique_compliments.add(inclusive_engine.generate_compliment())
    unique_compliments.add(action_based_engine.generate_compliment())
    unique_compliments.add(creative_engine.generate_compliment())
    unique_compliments.add(direct_praise_engine.generate_compliment())
    unique_compliments.add(short_engine.generate_compliment())
    unique_compliments.add(elegant_engine.generate_compliment())
    unique_compliments.add(superlative_engine.generate_compliment())

# Count the number of unique compliments
unique_compliment_count = len(unique_compliments)

# Print the total count of unique compliments
print(f"Total unique compliments generated: {unique_compliment_count}")
