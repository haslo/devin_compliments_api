from flask import Flask, jsonify
import random

app = Flask(__name__)

# Define compliment templates inspired by the analyzed list
compliment_templates = [
    "You're {adjective} than a {imaginary_thing}, because you're {reality_aspect}.",
    "Your {feature} is {compliment}.",
    "You have an {attribute} that {action}.",
    "Your {skill} is {positive_adjective}.",
    "You're so {trait} that {hyperbole}.",
    # ... add more templates up to 20
]

# Define dictionaries for each template component
adjectives = ['better', 'more amazing', 'making me happier']
imaginary_things = ['unicorn', 'shooting star', 'treasure']
reality_aspects = ['real', 'here', 'tangible']
features = ['smile', 'style', 'sense of humor']
compliments = ['contagious', 'impeccable', 'infectious']
attributes = ['energy', 'aura', 'presence']
actions = ['lights up the room', 'makes everyone smile', 'is captivating']
skills = ['creativity', 'dedication', 'work']
positive_adjectives = ['admirable', 'inspiring', 'remarkable']
traits = ['thoughtful', 'generous', 'kind']
hyperboles = ['you could light up the darkest of nights', 'you make the sun envious']

# Function to generate a random compliment from a template
def generate_compliment_from_template(template):
    compliment = template.format(
        adjective=random.choice(adjectives),
        imaginary_thing=random.choice(imaginary_things),
        reality_aspect=random.choice(reality_aspects),
        feature=random.choice(features),
        compliment=random.choice(compliments),
        attribute=random.choice(attributes),
        action=random.choice(actions),
        skill=random.choice(skills),
        positive_adjective=random.choice(positive_adjectives),
        trait=random.choice(traits),
        hyperbole=random.choice(hyperboles)
    )
    return compliment

@app.route('/compliment', methods=['GET'])
def generate_compliment():
    # Select a random template
    template = random.choice(compliment_templates)
    # Generate a compliment from the selected template
    compliment = generate_compliment_from_template(template)
    return jsonify({'compliment': compliment})

if __name__ == '__main__':
    app.run(debug=False)
