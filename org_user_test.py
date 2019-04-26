import json
import requests
import config


session = requests.session()
API_TOKEN = config.api_key


api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'python-requests/3.6.1',
           'Accept': 'application/vnd.github.v3+json',
           'Authorization': 'token %s' % API_TOKEN}


def test_org_user(target):
    api_url = '{}orgs/{}/repos'.format(api_url_base, target)
    # use session.get instead of request
    response = session.get(api_url, headers=headers)

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None