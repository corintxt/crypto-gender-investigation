import pandas as pd

from get_collaborators import get_all_contributions
from get_user_collaborators import get_user_org_contributions
import org_user_test
import parse_gender
import time

csv_file = input('Enter input csv file: > ')

organizations = pd.read_csv(csv_file)


for index, org in organizations.iterrows():
    try:
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
                
                # Test if set up as user or org
                if org_user_test.test_org_user(github_org):
                    get_all_contributions(github_org)
                else:
                    get_user_org_contributions(github_org)
            print("Updating input csv")
            organizations.loc[index, 'scraped'] = 'y'
            print("Pausing before next loop.")
            time.sleep(30)

        organizations.to_csv(csv_file, header=True, index=False)
        

    except KeyboardInterrupt:
        break
        print("Scraping stopped by user.")

print("SCRIPT COMPLETE.")