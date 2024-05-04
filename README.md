# Devin's Compliment API

## Overview
This project is a Python Flask API that generates random compliments directed at "you" (the reader of the compliment). The compliments are pieced together from different parts of sentences to form complete sentences, ensuring they are never inappropriate, racist, or sexist. The API is capable of generating millions of unique compliments with a few different grammatical structures and is designed to be fast and reliable. The sentence parts are stored in text files, and no database is used.

## Development Setup
To set up the development environment for this project, follow these steps:

1. Ensure Python 3.8+ is installed on your system.
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

## Testing
Test-Driven Development (TDD) is used throughout this project. To run the tests, use the following command:

```bash
python -m unittest discover -s tests
```

Ensure all tests pass before pushing changes to the repository.

## Contributing
Contributions are welcome! Please read the CONTRIBUTING.md file for guidelines on how to contribute to this project.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
