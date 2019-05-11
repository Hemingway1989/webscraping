import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

def basic_authentication(login):
    http_basic_auth = HTTPBasicAuth(login, getpass())
    return http_basic_auth
