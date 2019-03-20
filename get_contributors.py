import json
import requests

headers = {'Content-Type': 'application/json',
           'User-Agent': 'Python Student',
           'Accept': 'application/vnd.github.v3+json'}

# URL format:
# https://api.github.com/repos/recursecenter/blaggregator/contributors

def get_contributors(contrib_url):
    response = requests.get(contrib_url, headers=headers)

    if response.status_code == 200:
        return (response.json())
    else:
        print('[!] HTTP {0} calling repo [{1}]'.format(response.status_code, contrib_url))
        return None


