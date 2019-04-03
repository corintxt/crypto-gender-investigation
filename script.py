import pandas as pd

from get_collaborators import get_all_contributions
import parse_gender


organizations = pd.read_csv(
    input('Enter input csv file: > ')
    )

for org in organizations['github_org']:
    if type(org) == str: 
        print("""****SCRAPING:***** 
        {}
    *********************""".format(org))

        get_all_contributions(org)
    else:
        continue
        # skip over organizations with no github_org listed

print("SCRIPT COMPLETE.")

# Next run gender lookup on all csvs.