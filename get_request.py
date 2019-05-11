import requests
from requests.exceptions import HTTPError
from requests.exceptions import Timeout
from basic_authentication import basic_authentication

def get_request(url, response_format = None, timeout = (5, 5), authentication = False, login = None):
    # status code 1xx Information
    # status code 2xx Success - request was received, understood and accepted
    # status code 3xx Redirection
    # status code 4xx Client Errors
    # status code 5xx Server Errors

    # timeout parameter 1st: time to establish a connection, 2nd: time of waiting for response


    with requests.Session() as session:
        if authentication is True:
            session.auth = basic_authentication(login)

    try:
        response = session.get(url, timeout = timeout)
    except Timeout:
        print('The request timed out')
    except HTTPError as http_error:
        print(f'HTTP error occured: {http_error}')
    except Exception as other_error:
        print(f'Some other error occured: {other_error}')
    else:
        print(f'Request succeded! (Status code: {response.status_code})')

    if response_format == 'json':
        try:
            json_response = response.json()     # json dictionary
            return json_response
        except ValueError:                      # includes simplejson.decoder.JSONDecodeError
            print('Decoding JSON has failed')

    elif response_format == 'headers':
        headers_response = response.headers
        return headers_response

    elif response_format == 'binary':
        binary_response = response.content
        return binary_response

    elif response_format == 'text':
        text_response = response.text
        return text_response


# usage example
# url = 'https://github.com'
#
# get_request(url,
#             response_format = 'text',
#             timeout = (1, 1),
#             authentication = True,
#             login = 'Hemingway1989')
