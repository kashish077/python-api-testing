import json
import os

def load_config(env="dev"):
    config_path = os.path.join("data", f"{env}_config.json")
    with open(config_path) as f:
        return json.load(f)