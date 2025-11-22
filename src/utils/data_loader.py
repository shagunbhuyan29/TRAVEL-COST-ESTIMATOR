import json

class DataLoader:
    @staticmethod
    def load_json(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
