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
from engines.personal_quality_compliment_engine import PersonalQualityComplimentEngine
from engines.metaphor_compliment_engine import MetaphorComplimentEngine
from engines.action_based_compliment_engine import ActionBasedComplimentEngine
from engines.direct_praise_compliment_engine import DirectPraiseComplimentEngine
from engines.superlative_compliment_engine import SuperlativeComplimentEngine
from engine_selector import EngineSelector

app = Flask(__name__)

# List of compliment engine classes
engine_classes = [
    SimpleComplimentEngine,
    FeatureComplimentEngine,
    CreativeComplimentEngine,
    ImaginativeComplimentEngine,
    InspirationalComplimentEngine,
    WhimsicalComplimentEngine,
    AdmirationComplimentEngine,
    ElegantComplimentEngine,
    ShortComplimentEngine,
    PersonalQualityComplimentEngine,
    MetaphorComplimentEngine,
    ActionBasedComplimentEngine,
    DirectPraiseComplimentEngine,
    SuperlativeComplimentEngine
]

# Initialize EngineSelector with the list of engine classes
engine_selector = EngineSelector(engine_classes)

@app.route('/compliment', methods=['GET'])
def generate_compliment():
    # Select the next compliment engine in the cycle using EngineSelector
    engine_class = engine_selector.get_next_engine()
    engine = engine_class()
    compliment = engine.generate_compliment()
    # Print the name of the selected engine for debugging purposes
    print(f"Selected engine: {engine_class.__name__}")
    return jsonify({'compliment': compliment})

if __name__ == '__main__':
    app.run(debug=True)
