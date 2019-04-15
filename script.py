import pandas as pd

from get_user_collaborators import get_all_contributions
import parse_gender


organizations = pd.read_csv(
    input('Enter input csv file: > ')
    )


for index, org in organizations.iterrows():
    github_org = org['github_org']
    
    # current list of values to ignore
    scraped_values = ['y','n']
    
    if type(github_org) == str:
        if str(org['scraped']).lower() in scraped_values:
            continue
        else:
            print("****SCRAPING:*****")
            print('    {}'.format(github_org))
            print('*******************')
            get_all_contributions(github_org)

print("SCRIPT COMPLETE.")