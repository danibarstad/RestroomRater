import os
import requests
from .models import Venue
from django.db import IntegrityError


YELP_API_KEY = os.environ.get('YELP_API_KEY')


def get_location():
    """ user inputs zip code to search """
    
    return int(input('Enter your zip code: '))


def get_name(location):
    """ makes call to Yelp API and returns list of establishments within the given zip code """
    
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'location': f'{location}'
    }
    headers = {'Authorization': f'Bearer {YELP_API_KEY}'}

    try:
        response = requests.get(url, params=params, headers=headers).json()
        for venue in response['businesses']:
            venue_name = venue['name']
            venue_category = venue['categories'][1]['title']
            venue_address = venue['location']['address1']
            venue_city = venue['location']['city']
            venue_state = venue['location']['state']
            venue_zip = venue['location']['zip_code']
            venue_image = venue['image_url']
            new_venue = Venue(
                name=venue_name, 
                category=venue_category,
                address=venue_address, 
                city=venue_city, 
                state=venue_state, 
                zip_code=venue_zip, 
                image=venue_image)
            new_venue.save()
    
    except IntegrityError as e:
        print('duplicate entry added')
        print(e)