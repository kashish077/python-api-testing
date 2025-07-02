from utils.config_loader import load_config
from utils.requests_helper import APIClient

def test_get_post_by_id():
    config = load_config("dev")
    client = APIClient(config["base_url"])
    response = client.get("/posts/1")

    assert response.status_code == 200
    json_data = response.json()
    assert "title" in json_data
    assert json_data["id"] == 1