import requests
import json


api_url_base = 'https://api.genderize.io/'

def get_gender(firstname):
    request_url = '{}?name={}'.format(api_url_base, firstname)
    response = requests.get(request_url)
    
    if response.status_code == 200:
        return (response.json())
    else:
        print('[!] HTTP {0} looking up name [{1}]'.format(response.status_code, firstname))
        return None