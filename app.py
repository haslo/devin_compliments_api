from flask import Flask, jsonify
from engine_selector import EngineSelector

app = Flask(__name__)

# Initialize EngineSelector
engine_selector = EngineSelector()

@app.route('/compliment', methods=['GET'])
def generate_compliment():
    # Select the next compliment engine in the cycle using EngineSelector
    engine_class = engine_selector.get_next_engine()
    engine = engine_class()
    compliment = engine.generate_compliment()
    return jsonify({'compliment': compliment})

if __name__ == '__main__':
    app.run(debug=True)
