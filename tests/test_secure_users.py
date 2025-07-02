from utils.config_loader import load_config
from utils.auth_helper import get_auth_token
from utils.requests_helper import APIClient
import pytest

@pytest.mark.auth
def test_get_users_authenticated():
    config = load_config("secure")
    token = get_auth_token(config["base_url"], config["email"], config["password"])
    client = APIClient(config["base_url"], token=token)

    response = client.get("/users?page=2")
    assert response.status_code == 200
    json_data = response.json()
    assert "data" in json_data
