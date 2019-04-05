import json
import requests
import config

session = requests.session()

API_TOKEN = config.api_key

api_limit_url = 'https://api.github.com/rate_limit'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'python-requests/3.6.1',
           'Accept': 'application/vnd.github.v3+json',
           'Authorization': 'token %s' % API_TOKEN}

limit = session.get(api_limit_url)

remaining = limit.json()['resources']

print(f'''
------------
GraphQL request status:
{remaining}
------------''')