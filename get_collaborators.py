import json
import requests
import csv
import config
import time

session = requests.session()
## Comment out Tor proxy for now.
# session.proxies = {}
# session.proxies['http'] = 'socks5h://localhost:9050'
# session.proxies['https'] = 'socks5h://localhost:9050'

API_TOKEN = config.api_key

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
    path = repo['full_name']
    
    response = session.get('{}repos/{}/stats/contributors'.format(api_url_base, path), headers=headers)

    if response.status_code == 200:
        return (
            # returns `contribution_response`
            {'name': name,
             'data': response.json()}
        )
    elif response.status_code == 202:
        print("Response 202: Accepted/Waiting")
        time.sleep(1)
        return (
            {'name': name,
             'data': response.json()}
        )
    elif response.status_code == 204:
        print("Response 204: No data in repo {}".format(path))
        return None
    else:
        print('[!] HTTP {0} calling repo [{1}]'.format(response.status_code, path))
        time.sleep(1)
        print("Re-attempting...")
        get_contributors(repo)
        # return None // currently this creates a loop


def build_contributor_list(contribution_response):
    all_repo_contributions = list()
    
    # This will throw a TypeError if ['data'] is empty
    for i in range(0,len(contribution_response['data'])):
        ctr = dict()
        ctr["repo"] = contribution_response['name']
        ctr["username"] = contribution_response['data'][i]['author']['login']
        ctr["contributions"] = contribution_response['data'][i]['total']
        ctr["avatar_url"] = contribution_response['data'][i]['author']['avatar_url']
        ctr["profile_url"] = contribution_response['data'][i]['author']['url']
        all_repo_contributions.append(ctr)
    
    return all_repo_contributions


def lookup_human_name(profile_url):    
    response = session.get(profile_url, headers=headers)

    if response.status_code == 200:
        return (response.json()['name'])
    else:
        print('[!] HTTP {0} looking up user [{1}]'.format(response.status_code, profile_url))
        return None


def append_list_to_csv(mylist, output_file):
    with open(output_file, 'a') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(mylist)

# define list variable outside of get_all_contributions function
all_org_contributions = list()
  
def get_all_contributions(org):
    print("Retrieving list of all repos for {}".format(org))
    repos = get_repos(org)

    for repo in repos:
        print("Building contributor commit list for {}".format(repo['full_name']))
        contributors = get_contributors(repo)
        if contributors:
            contribution_list = build_contributor_list(contributors)
            all_org_contributions.append(contribution_list)
        else:
            continue

    # new API call to add real names to dictionary
    print("Matching real names against contributor usernames...")
    
    for i in range (0, len(all_org_contributions)):
        print("Searching repo {} of {}".format(i,len(all_org_contributions)))
        for j in range (0, len(all_org_contributions[i])):
            human_name = lookup_human_name(all_org_contributions[i][j]['profile_url'])
            all_org_contributions[i][j]['name'] = human_name

    print("Contribution list complete!")

## Write to file
    print("Writing to file.")

    file_name = "./data/{}.csv".format(org)
    flat_contributions = [item for sublist in all_org_contributions for item in sublist]
    ## Do this row by row.
    for item in flat_contributions:
        append_list_to_csv(item.values(), file_name)

    print("Contributor list saved as {}".format(file_name))

if __name__ == '__main__':
    target_repo = input('Enter name of org to scrape: > ')
    get_all_contributions(target_repo)