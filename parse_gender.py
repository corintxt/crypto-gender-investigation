import requests
import json
import config
import pandas as pd


api_url_base = 'https://api.genderize.io/'

def get_gender(firstname):
    request_url = '{}?apikey={}&name={}'.format(api_url_base, config.genderize_key, firstname)
    response = requests.get(request_url)
    print("Genderizing name: {}".format(firstname))
    
    if response.status_code == 200:
        return (response.json())
    else:
        print('[!] HTTP {0} looking up name [{1}]'.format(response.status_code, firstname))
        return None


def lookup_genders(csv, output):
    df = pd.read_csv(csv, names=['repo', 'username', 'contributions', 
                'avatar_url', 'profile_url', 'real_name'])

    gender_list = list()

    for name in df['real_name'].unique():
        if type(name) == str: # don't call on NaN values (which are float)
            if name[0].isspace():
                name = name[1:]
            first_name = name.split(' ')[0]
            gender_result = get_gender(first_name)
            gender_result['real_name'] = name # add real name back to dictionary
            gender_list.append(gender_result)      

    # Convert to dataframe and merge with data from original csv
    gender_df = pd.DataFrame(gender_list)
    full_frame = pd.merge(df, gender_df[['real_name', 'gender', 'probability']], 
               on='real_name', how='outer')

    full_frame.to_csv(output, index=False, header=False)

if __name__ == '__main__':
    target_csv = str(input('Enter csv file to genderize: > '))
    lookup_genders(target_csv, './gendered/{}'.format(target_csv))