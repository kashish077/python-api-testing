import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        return self.session.post(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, json=None, **kwargs):
        return self.session.put(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)
