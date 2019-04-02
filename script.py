import pandas as pd

from get_contributions import get_all_contributions
import parse_gender


organizations = pd.read_csv(
    input('Enter input csv file: > ')
    )

for org in organizations['github_org']:
    print("""****SCRAPING:***** 
    {}
*********************""".format(org))

    get_all_contributions(org)

print("SCRIPT COMPLETE.")

# Next run gender lookup on all csvs.