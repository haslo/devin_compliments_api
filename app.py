import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify
from engine_selector import EngineSelector
from dictionary_loader import DictionaryLoader

# Set up detailed logging to capture all levels of logs
logging.basicConfig(level=logging.INFO)

# Create a file handler to log messages to a file
file_handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))

# Add the file handler to the root logger
logging.getLogger().addHandler(file_handler)

app = Flask(__name__)

# Load dictionaries once at the start of the application
dictionary_loader = DictionaryLoader('compliment_dictionaries.yaml')
dictionaries = dictionary_loader.load_dictionaries()

@app.route('/compliment', methods=['GET'])
def generate_compliment():
    try:
        logging.debug('Generating a compliment...')
        engine_selector = EngineSelector.singleton()
        # Select the next compliment engine in the cycle using EngineSelector
        engine_class = engine_selector.get_next_engine()
        logging.debug(f'Using engine: {engine_class.__name__}')
        # Pass the loaded dictionaries to the engine instance
        engine = engine_class(dictionaries)
        compliment = engine.generate_compliment()
        logging.debug(f'Generated compliment: {compliment}')
        return jsonify({'compliment': compliment})
    except Exception as e:
        logging.error(f'Error generating compliment: {e}', exc_info=True)
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=False)
