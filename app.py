import logging
from flask import Flask, jsonify
from engine_selector import EngineSelector
from dictionary_loader import DictionaryLoader
# Removed the DirectPraiseComplimentEngine import as it's not used directly here

# Set up basic logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Load dictionaries once at the start of the application
dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

@app.route('/compliment', methods=['GET'])
def generate_compliment():
    try:
        logging.info('Generating a compliment...')
        engine_selector = EngineSelector.singleton()
        # Select the next compliment engine in the cycle using EngineSelector
        engine_class = engine_selector.get_next_engine()
        logging.info(f'Using engine: {engine_class.__name__}')
        # Pass the loaded dictionaries to the engine instance
        engine = engine_class(dictionaries)
        compliment = engine.generate_compliment()
        logging.info(f'Generated compliment: {compliment}')
        return jsonify({'compliment': compliment})
    except Exception as e:
        logging.error(f'Error generating compliment: {e}', exc_info=True)
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=False)
