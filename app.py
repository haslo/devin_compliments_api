from flask import Flask, jsonify
import random

app = Flask(__name__)

def get_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    return random.choice(lines)

@app.route('/compliment', methods=['GET'])
def generate_compliment():
    subject = get_random_line('dictionaries/subjects.txt')
    verb = get_random_line('dictionaries/verbs.txt')
    adjective = get_random_line('dictionaries/adjectives.txt')
    object_ = get_random_line('dictionaries/objects.txt')
    adverb = get_random_line('dictionaries/adverbs.txt')

    compliment = f"{subject} {verb} {adverb} {adjective} {object_}."
    return jsonify({'compliment': compliment})

if __name__ == '__main__':
    app.run(debug=False)
