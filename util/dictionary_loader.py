import yaml
import os

class DictionaryLoader:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def load_dictionaries(self):
        dictionaries = {}
        try:
            for filename in os.listdir(self.directory_path):
                if filename.endswith('_dictionary.yaml'):
                    engine_name = filename.replace('_dictionary.yaml', '')
                    with open(os.path.join(self.directory_path, filename), 'r') as file:
                        dictionaries[engine_name] = yaml.safe_load(file)
            return dictionaries
        except FileNotFoundError:
            raise FileNotFoundError(f"The directory {self.directory_path} was not found.")
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML file: {e}")
