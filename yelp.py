import os
import requests

loc = 'Georgetown'  # TODO: change to get location as user input
enVar = os.environ.get('YELP_API_KEY')
business_id = 'WavvLdfdP6g8aZTtbBQHTw'
url = 'https://api.yelp.com/v3/businesses/search'
params = {
    'location': f'{loc}',
    'limit': 1
}
headers = {'Authorization': 'Bearer %s' % enVar}

data = requests.get(url, params=params, headers=headers).json()
# print(data)
name = data['businesses'][0]['name']
print(f'The name of the establishment is: {name}')