import requests
from requests.exceptions import HTTPError

def get_request(url, response_format = None):
    # status code 1xx Information
    # status code 2xx Success - request was received, understood and accepted
    # status code 3xx Redirection
    # status code 4xx Client Errors
    # status code 5xx Server Errors

    try:
        response = requests.get(url)
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
# url = 'https://axa.csod.com'
#
# get_request(url, 'text')
