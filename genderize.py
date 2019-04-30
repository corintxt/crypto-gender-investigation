import os
from parse_gender import lookup_genders

target_directory = '/home/corin/Dropbox/CODE/RC/Crypto-Scraper/data/commits/'

directory = os.fsencode(target_directory)

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".csv"):
        print("Finding genders for:")
        print(filename)
        print("~~~~~~~~~~~~~~~~~~")
        csv = target_directory + filename
        lookup_genders(csv, './data/gendered/{}'.format(filename))
        os.rename(csv, target_directory + "processed/" + filename)
     else:
         continue

print("GENDER INFERENCE COMPLETE.")

# Note - might need to add timeout to not reach API limit