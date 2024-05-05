from flask import Flask, jsonify
from engines.simple_compliment_engine import SimpleComplimentEngine
from engines.feature_compliment_engine import FeatureComplimentEngine
from engines.creative_compliment_engine import CreativeComplimentEngine
from engines.imaginative_compliment_engine import ImaginativeComplimentEngine
from engines.inspirational_compliment_engine import InspirationalComplimentEngine
from engines.whimsical_compliment_engine import WhimsicalComplimentEngine
from engines.admiration_compliment_engine import AdmirationComplimentEngine
from engines.elegant_compliment_engine import ElegantComplimentEngine
from engines.short_compliment_engine import ShortComplimentEngine
import random

app = Flask(__name__)

# Tracking the selection frequency of each engine
engine_selection_tracker = {
    'SimpleComplimentEngine': 0,
    'FeatureComplimentEngine': 0,
    'CreativeComplimentEngine': 0,
    'ImaginativeComplimentEngine': 0,
    'InspirationalComplimentEngine': 0,
    'WhimsicalComplimentEngine': 0,
    'AdmirationComplimentEngine': 0,
    'ElegantComplimentEngine': 0,
    'ShortComplimentEngine': 0
}

@app.route('/compliment', methods=['GET'])
def generate_compliment():
    # Randomly select a compliment engine
    engine_class = random.choice([
        SimpleComplimentEngine,
        FeatureComplimentEngine,
        CreativeComplimentEngine,
        ImaginativeComplimentEngine,
        InspirationalComplimentEngine,
        WhimsicalComplimentEngine,
        AdmirationComplimentEngine,
        ElegantComplimentEngine,
        ShortComplimentEngine
    ])
    # Increment the selection count for the chosen engine
    engine_selection_tracker[engine_class.__name__] += 1
    engine = engine_class()
    compliment = engine.generate_compliment()
    return jsonify({'compliment': compliment})

if __name__ == '__main__':
    app.run(debug=True)
