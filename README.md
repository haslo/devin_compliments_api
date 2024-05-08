# Devin's Compliment API

## Overview
This project is a Python Flask API that generates random compliments directed at "you" (the reader of the compliment). The compliments are pieced together from different parts of sentences to form complete sentences, ensuring they are never inappropriate, racist, or sexist. The API is capable of generating millions of unique compliments with a few different grammatical structures and is designed to be fast and reliable. The sentence parts are stored in text files, and no database is used.

## Development Setup
To set up the development environment for this project, follow these steps:

1. Ensure Python 3.10 or later is installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the cloned repository directory.
4. Create a virtual environment with `python -m venv venv`.
5. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
6. Install the required dependencies with `pip install -r requirements.txt`.
7. Run the Flask application with `flask run`.

## API Usage
To interact with the API, send a GET request to the `/compliment` endpoint. The API will return a JSON object containing a random compliment.

Example request:
```
GET /compliment HTTP/1.1
Host: <API_HOST>
```

Example response:
```json
{
  "compliment": "You always bring out the best in others."
}
```

## Generator Scripts
The `generate_examples` directory contains scripts that generate example compliments using the different engines. To run these scripts, ensure the virtual environment is activated and execute the following command from the project root:
```bash
python3 -m generate_examples.<script_name>
```
Replace `<script_name>` with the name of the script you wish to run (e.g., `generate_feature_examples`).

## Project Structure
The project has been reorganized to include a `util` module, which contains utility files such as `compliment_dictionaries.yaml`, `dictionary_loader.py`, and `engine_selector.py`. This reorganization aims to improve the modularity and maintainability of the codebase.

## User Acceptance Testing
To perform user acceptance testing, follow these steps:

1. Ensure the Flask application is running by executing `flask run`.
2. Send a GET request to the `/compliment` endpoint using a tool like `curl` or Postman.
3. Verify that the response contains a `compliment` field with a string value.
4. Test multiple requests to ensure a variety of compliments are generated.
5. Confirm that the compliments are appropriate and adhere to the project's guidelines.

Example command for testing with `curl`:
```
curl -X GET http://localhost:5000/compliment
```

## Testing
Test-Driven Development (TDD) is used throughout this project. To run the tests, execute the following command from the repository root:
```bash
pytest
```
Ensure all tests pass before pushing changes to the repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
