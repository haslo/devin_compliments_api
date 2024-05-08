import yaml

class DictionaryLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_dictionaries(self):
        try:
            with open(self.file_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.file_path} was not found.")
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML file: {e}")
