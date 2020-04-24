import os
import requests

enVar = os.environ.get('YELP_API_KEY')
url = 'https://api.yelp.com/v3/businesses/'
params = {'id':'WavvLdfdP6g8aZTtbBQHTw'}
headers = {'Authorization': f'Bearer {enVar}'}

data = requests.get(url, params=params, headers=headers).json()
print(data)
# name = data['name']
# print(f'The name of the establishment is: {name}')