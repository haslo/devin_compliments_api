from flask import Flask, jsonify
from engines.simple_compliment_engine import SimpleComplimentEngine
from engines.feature_compliment_engine import FeatureComplimentEngine
from engines.imaginative_compliment_engine import ImaginativeComplimentEngine
import random

app = Flask(__name__)

@app.route('/compliment', methods=['GET'])
def generate_compliment():
    # Randomly select a compliment engine
    engine_class = random.choice([SimpleComplimentEngine, FeatureComplimentEngine, ImaginativeComplimentEngine])
    engine = engine_class()
    compliment = engine.generate_compliment()
    return jsonify({'compliment': compliment})

if __name__ == '__main__':
    app.run(debug=False)
