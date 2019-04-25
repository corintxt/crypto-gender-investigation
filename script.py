import pandas as pd

from get_collaborators import get_all_contributions
from get_user_collaborators import get_user_org_contributions
import org_user_test
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
            if org_user_test.test_org_user(github_org): #test if user or org
                get_all_contributions(github_org)
            else:
                get_user_org_contributions(github_org)

print("SCRIPT COMPLETE.")