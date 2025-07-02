import requests

def get_auth_token(base_url, email, password):
    response = requests.post(f"{base_url}/login", json={
        "email": email,
        "password": password
    })
    assert response.status_code == 200, f"Login failed: {response.text}"
    return response.json().get("token")

class APIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.session = requests.Session()
        if token:
            self.session.headers.update({
                "Authorization": f"Bearer {token}"
            })

    def get(self, endpoint, **kwargs):
        return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        return self.session.post(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, json=None, **kwargs):
        return self.session.put(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)

