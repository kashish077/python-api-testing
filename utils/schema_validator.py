import json
import os
from jsonschema import validate, ValidationError

def load_schema(filename):
    path = os.path.join("data", filename)
    with open(path) as f:
        return json.load(f)

def validate_response_schema(response_json, schema):
    try:
        validate(instance=response_json, schema=schema)
        return True
    except ValidationError as e:
        print(f"Schema validation error: {e}")
        return False
