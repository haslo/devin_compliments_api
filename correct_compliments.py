import json

# Define the corrections to be made: index and new compliment
corrections = {
    1: 'Your mindset is a beacon of intelligence, shining with considerate wisdom.',
    6: "You're as captivating as a melody and as mysterious as an enchanted forest, embodying a magnetic charm.",
    8: "In the realm of a griffin's majesty, you reign with sincere enchantment.",
    17: 'Your mindset is as genuine as it is wise, a true marvel to behold.',
    19: 'You influence like a rainbow, compassionate and full of enthusiasm.'
}

# Load the compliments from the existing file
with open('twenty_compliments.txt', 'r') as file:
    compliments = json.load(file)

# Apply the corrections
for idx, correction in corrections.items():
    compliments[idx - 1]['compliment'] = correction

# Write the corrected compliments to a new file
with open('twenty_compliments_corrected.txt', 'w') as outfile:
    json.dump(compliments, outfile, indent=4)
