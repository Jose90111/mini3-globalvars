import requests

class OnlineVars:
    def __init__(self, base_url="http://127.0.0.1:5000"):
        self.base_url = base_url.rstrip('/')

    def _request(self, method, path, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = requests.request(method, url, **kwargs)
        return response

    def list(self):
        response = self._request("GET", "/")
        return response.json() if response else None

    def get(self, name):
        response = self._request("GET", name)
        return response.json() if response else None

    def set(self, name, value):
        response = self._request(
            "POST",
            name,
            data=str(value),
            headers={'Content-Type': 'text/plain'}
        )
        if response:
            return response.status_code, response.text
        return None, None

    def rem(self, name):
        response = self._request("DELETE", name)
        if response and response.status_code == 200:
            return True
        return False