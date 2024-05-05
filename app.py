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
    engine = engine_class()
    compliment = engine.generate_compliment()
    return jsonify({'compliment': compliment})

if __name__ == '__main__':
    app.run(debug=False)
