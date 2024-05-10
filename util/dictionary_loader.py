import yaml
import os

class DictionaryLoader:
    def __init__(self, directory_path, dictionary_name):
        self.directory_path = directory_path
        self.dictionary_name = dictionary_name

    def load_dictionary(self):
        dictionary_path = os.path.join(self.directory_path, f"{self.dictionary_name}_dictionary.yaml")
        try:
            with open(dictionary_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The dictionary file {dictionary_path} was not found.")
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML file: {e}")
