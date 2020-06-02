import os
import requests
from .models import Establishment
from django.db import IntegrityError

YELP_KEY = os.environ.get('YELP_API_KEY')

def get_location():
    """ user inputs zip code to search """
    
    return int(input('Enter your zip code: '))

def get_name(location):
    """ makes call to Yelp API and returns list of establishments within the given zip code """
    venues = []
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'location': f'{location}'
    }
    headers = {'Authorization': f'Bearer {YELP_KEY}'}

    try:
        response = requests.get(url, params=params, headers=headers).json()
        for venue in response['businesses']:
            venues.append(venue['name'])

            venue_name = venue['name']
            venue_city = venue['city']
            venue_city = venue['state']
            new_venue = Establishment(name=venue_name, city=venue_city, state=venue_state)
            new_venue.save()
    
    except IntegrityError as e:
        print('duplicate entry added')
        print(e)

    return venues