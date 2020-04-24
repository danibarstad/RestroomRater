import os
import requests

YELP_KEY = os.environ.get('YELP_API_KEY')

def get_location():
    return input('Enter your zip code: ')

def get_name(location):
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'location': f'{location}',
        'limit': 1
    }
    headers = {'Authorization': f'Bearer {YELP_KEY}'}

    data = requests.get(url, params=params, headers=headers).json()
    return data['businesses'][0]['name']