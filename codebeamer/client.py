import requests, json
from .mixins.project import ProjectMixin


class Codebeamer(ProjectMixin):
    
    def __init__(self, url, login, password):
        self.base_url = url
        self.auth = (login, password)

    def get(self, uri):
        url = self.base_url + uri
        res = requests.get(url, auth=self.auth, verify=True)
        if res.status_code == 200:
            return json.loads(res.content)
        else:
            print(f"Warning : GET error ({url})")
            return None

    def put(self, uri, data):
        url = self.base_url + uri
        res = requests.put(url, json=data, auth=self.auth, verify=True)
        if res.status_code == 200:
            return json.loads(res.content)
        else:
            print(f"Warning : PUT error ({url})")
            return None

    def post(self, uri, data):
        url = self.base_url + uri
        res = requests.post(url, json=data, auth=self.auth, verify=True)
        if res.status_code == 201:
            return json.loads(res.content)
        else:
            print(f"Warning : POST error ({url})")
            return None
