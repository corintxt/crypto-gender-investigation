import json
import requests

api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'request',
           'Accept': 'application/vnd.github.v3+json'}

def get_repos(orgname):
    api_url = '{}orgs/{}/repos'.format(api_url_base, orgname)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return (response.json())
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None


def get_contributors(repo):
    name = repo['name']
    contrib_url = repo['contributors_url']
    
    response = requests.get(contrib_url, headers=headers)

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
        all_repo_contributions.append(ctr)
    
    return all_repo_contributions


all_org_contributions = list()
    
def get_all_contributions(org):
    repos = get_repos(org)

    for repo in repos:
        contributors = get_contributors(repo)
        contribution_list = build_contribution_list(contributors)
        all_org_contributions.append(contribution_list)