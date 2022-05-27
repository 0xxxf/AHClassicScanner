import requests

class APICaller:
    def __init__(self, headers, token=None):
        self.token = token
        self.headers = headers

    def request(self, url):
        res = requests.get(url, params=self.headers)
        return res.status_code

    def requestJSON(self, url):
        res = requests.get(url, params=self.headers)
        return res.json()
 
