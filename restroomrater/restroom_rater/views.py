# import requests
from django.shortcuts import render, redirect, get_object_or_404
from .forms import get_zip
from . import yelp_api
from .models import Venue

# Create your views here.

def homepage(request):
    new_zip_form = get_zip()

    return render(request, 'restroom_rater/homepage.html', { 'new_zip_form': new_zip_form })


def venue_list(request):
    new_zip_form = get_zip()
    search_zip = request.GET.get('zip_code')

    if not Venue.objects.filter(zip_code=search_zip).exists():
        venues = yelp_api.get_name(search_zip)
        venues = Venue.objects.filter(zip_code=search_zip).order_by('name')
    else:
        # venues = Venue.objects.all().order_by('name')
        venues = Venue.objects.filter(zip_code=search_zip).order_by('name')

    return render(request, 'restroom_rater/venue_list.html', { 'venues': venues, 'new_zip_form': new_zip_form, 'search_zip': search_zip})


def venue_detail(request, venue_pk):
    venue = get_object_or_404(Venue, pk=venue_pk)
    return render(request, 'restroom_rater/venue_detail.html', {'venue': venue})