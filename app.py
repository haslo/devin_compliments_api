from flask import Flask, jsonify
from compliment_engines import SimpleComplimentEngine, FeatureComplimentEngine
import random

app = Flask(__name__)

@app.route('/compliment', methods=['GET'])
def generate_compliment():
    # Randomly select a compliment engine
    engine_class = random.choice([SimpleComplimentEngine, FeatureComplimentEngine])
    engine = engine_class()
    compliment = engine.generate_compliment()
    return jsonify({'compliment': compliment})

if __name__ == '__main__':
    app.run(debug=False)
