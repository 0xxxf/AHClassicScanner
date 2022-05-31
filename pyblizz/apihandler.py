import requests
import definitions


class APICaller:
    def __init__(self, namespace, token=None):
        # TODO: Check for valid token on class initialization
        self.token = token
        self.namespace = None
        self.region = None
        self.locale = None
        self.status = 0

    def request(self, url):
        res = requests.get(url, params=self.headers)
        self.status = res.status_code
        return res.status_code

    def requestJSON(self, url):
        res = requests.get(url, params=self.headers)
        self.status = res.status_code
        return res.json()

    def updateToken(self, token):
        self.token = token
        # TODO: Check if the token is valid by making a call
