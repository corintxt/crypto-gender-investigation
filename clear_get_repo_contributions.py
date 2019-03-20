import json
import requests
import os

session = requests.session()
## Comment out Tor proxy for now.
# session.proxies = {}
# session.proxies['http'] = 'socks5h://localhost:9050'
# session.proxies['https'] = 'socks5h://localhost:9050'

API_token = os.getenv("your_api_token_env_var")

api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'python-requests/3.6.1',
           'Accept': 'application/vnd.github.v3+json',
           'Authorization': 'token %s' % API_TOKEN}


def get_repos(orgname):
    api_url = '{}orgs/{}/repos'.format(api_url_base, orgname)
    # use session.get instead of request
    response = session.get(api_url, headers=headers)

    if response.status_code == 200:
        return (response.json())
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None


def get_contributors(repo):
    name = repo['name']
    contrib_url = repo['contributors_url']
    
    response = session.get(contrib_url, headers=headers)

    if response.status_code == 200:
        return (
            # returns `contribution_response`
            {'name': name,
             'data': response.json()}
        )
    else:
        print('[!] HTTP {0} calling repo [{1}]'.format(response.status_code, contrib_url))
        return None


def build_contribution_list(contribution_response):
    all_repo_contributions = list()

    for i in range(0,len(contribution_response['data'])):
        ctr = dict()
        ctr["repo"] = contribution_response['name']
        ctr["username"] = contribution_response['data'][i]['login']
        ctr["contributions"] = contribution_response['data'][i]['contributions']
        ctr["avatar_url"] = contribution_response['data'][i]['avatar_url']
        ctr["profile_url"] = contribution_response['data'][i]['url']
        all_repo_contributions.append(ctr)
    
    return all_repo_contributions


def lookup_human_name(profile_url):
    # restate headers in case I need to change
    lookup_headers = {'Content-Type': 'application/json',
           'User-Agent': 'python-requests/3.6.1',
           'Accept': 'application/vnd.github.v3+json'}
    
    response = session.get(profile_url, headers=lookup_headers)

    if response.status_code == 200:
        return (response.json()['name'])
    else:
        print('[!] HTTP {0} looking up user [{1}]'.format(response.status_code, profile_url))
        return None

# define list variable outside of get_all_contributions function
all_org_contributions = list()
  
def get_all_contributions(org):
    repos = get_repos(org)

    for repo in repos:
        contributors = get_contributors(repo)
        contribution_list = build_contribution_list(contributors)
        all_org_contributions.append(contribution_list)

    # new API call to add real names to dictionary
    for i in range (0, len(all_org_contributions)):
        for j in range (0, len(all_org_contributions[i])):
            human_name = lookup_human_name(all_org_contributions[i][j]['profile_url'])
            all_org_contributions[i][j]['name'] = human_name

    print("Contribution list complete.")