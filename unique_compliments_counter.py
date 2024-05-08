import random
import yaml
from engines.direct_praise_compliment_engine import DirectPraiseComplimentEngine
from engines.whimsical_compliment_engine import WhimsicalComplimentEngine
# Assuming there is an ImaginativeComplimentEngine similar to the other two engines
from engines.imaginative_compliment_engine import ImaginativeComplimentEngine

# Load the dictionaries from the compliment_dictionaries.yaml file
with open('compliment_dictionaries.yaml', 'r') as file:
    dictionaries = yaml.safe_load(file)

# Instantiate the compliment engine classes with the loaded dictionaries
direct_praise_engine = DirectPraiseComplimentEngine(dictionaries)
whimsical_engine = WhimsicalComplimentEngine(dictionaries)
# Assuming the ImaginativeComplimentEngine is implemented
imaginative_engine = ImaginativeComplimentEngine(dictionaries)

# Create a set to store unique compliments
unique_compliments = set()

# Define the number of iterations for generating compliments
iterations = 1000000  # Adjust the number as needed to estimate uniqueness

# Loop to generate compliments and add to the set
for _ in range(iterations):
    unique_compliments.add(direct_praise_engine.generate_compliment())
    unique_compliments.add(whimsical_engine.generate_compliment())
    unique_compliments.add(imaginative_engine.generate_compliment())

# Count the number of unique compliments
unique_compliment_count = len(unique_compliments)

# Print the total count of unique compliments
print(f"Total unique compliments generated: {unique_compliment_count}")
