import json
import requests
import csv
import config
import time
import datetime

session = requests.session()
## Uncomment for Tor proxy.
# session.proxies = {}
# session.proxies['http'] = 'socks5h://localhost:9050'
# session.proxies['https'] = 'socks5h://localhost:9050'

API_TOKEN = config.api_key

api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'python-requests/3.6.1',
           'Accept': 'application/vnd.github.v3+json',
           'Authorization': 'token %s' % API_TOKEN}

# modified version for users
def get_repos(orgname):
    api_url = '{}users/{}/repos?type=source'.format(api_url_base, orgname)
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
        print("Response OK: returned {} records".format(len(response.json())))
        return (
            # returns `contribution_response`
            { 'retry': False,
              'empty': False,
              'name': name,
             'data': response.json()}
        )
    elif response.status_code == 202:
        print("Response 202: Accepted/Generating data")
        return {'retry': True}
    elif response.status_code == 204:
        print("Response 204: No data in repo {}".format(path))
        return {'retry': False,
                'empty': True}
    else:
        print('[!] HTTP {0} calling repo [{1}]'.format(response.status_code, path))
        time.sleep(1)
        print("Re-attempting...")
        get_contributors(repo)


def build_contributor_list(contribution_response):
    all_repo_contributions = list()
    
    # TypeError returned if ['data'] is empty for a given repo
    for i in range(0,len(contribution_response['data'])):
        ctr = dict()
        ctr["repo"] = contribution_response['name']
        try:
            ctr["username"] = contribution_response['data'][i]['author']['login']
            ctr["contributions"] = contribution_response['data'][i]['total']
            ctr["avatar_url"] = contribution_response['data'][i]['author']['avatar_url']
            ctr["profile_url"] = contribution_response['data'][i]['author']['url']
        except TypeError:
            print("Repo did not return contributor data. Skipping.")
        else:
            all_repo_contributions.append(ctr)
    
    return all_repo_contributions


def lookup_human_name(profile_url):    
    response = session.get(profile_url, headers=headers)

    if response.status_code == 200:
        return (response.json()['name'])
    elif response.status_code == 403:
        print("Response 403: Forbidden")
        currentDT = datetime.datetime.now()
        print("Scraping stopped at {}".format(currentDT))
        print("Try again in one hour")
        quit()
    else:
        print('[!] HTTP {0} looking up user [{1}]'.format(response.status_code, profile_url))
        return None


def append_list_to_csv(mylist, output_file):
    with open(output_file, 'a') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(mylist)

# define list variable outside of get_all_contributions function
all_org_contributions = list()
  
def get_user_org_contributions(org):
    print("Retrieving list of source repos for {}".format(org))
    repos = get_repos(org)
    print("Found {} repos".format(len(repos)))

    for repo in repos:
        print("Building contributor commit list for {}".format(repo['full_name']))
        
        processing_loop = True

        while processing_loop:
            contributors = get_contributors(repo)
            if contributors['retry']:
                print("Waiting 10s to reattempt.")
                time.sleep(10)
                continue
            elif contributors['empty']:
                processing_loop = False
                continue
            else:    
                contribution_list = build_contributor_list(contributors)
                all_org_contributions.append(contribution_list)
                processing_loop = False
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

    file_name = "./data/commits/{}.csv".format(org)
    flat_contributions = [item for sublist in all_org_contributions for item in sublist]
    ## Do this row by row.
    for item in flat_contributions:
        append_list_to_csv(item.values(), file_name)

    print("Contributor list saved as {}".format(file_name))

if __name__ == '__main__':
    target_repo = input('Enter name of user to scrape: > ')
    get_user_org_contributions(target_repo)