import os
import requests

YELP_KEY = os.environ.get('YELP_API_KEY')

def get_location():
    """ user inputs zip code to search """
    
    return input('Enter your zip code: ')

def get_name(location):
    """ makes call to Yelp API and returns list of establishments within the given zip code """
    restaurants = []
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'location': f'{location}'
    }
    headers = {'Authorization': f'Bearer {YELP_KEY}'}

    response = requests.get(url, params=params, headers=headers).json()
    for business in response['businesses']:
        restaurants.append(business['name'])

    return restaurants