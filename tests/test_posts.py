import pytest
from utils.config_loader import load_config
from utils.requests_helper import APIClient
from utils.data_loader import load_test_data
from utils.schema_validator import load_schema, validate_response_schema


config = load_config("dev")
client = APIClient(config["base_url"])

test_data = load_test_data("test_posts.json")

@pytest.mark.parametrize("payload", test_data)
def test_create_post_data_driven(payload):
    response = client.post("/posts", json=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["title"] == payload["title"]
    assert json_data["body"] == payload["body"]
    assert json_data["userId"] == payload["userId"]

def test_get_post_schema():
    response = client.get("/posts/1")
    assert response.status_code == 200
    json_data = response.json()

    schema = load_schema("post_schema.json")
    assert validate_response_schema(json_data, schema)
