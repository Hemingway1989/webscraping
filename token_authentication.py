import requests
from requests.auth import AuthBase

class TokenAuthentication(AuthBase):
    # Implements a custom authentication scheme

    def __init__(self, token):
        self.token = token

    def __call__(self, api):
        # Attach an API to custom auth header
        api.headers['X-TokenAuth'] = f'{self.token}'
        return api

# how to use
# url = 'https://github.com/user'
# response = requests.get(url, auth = TokenAuthentication('1234abcde-token'))
