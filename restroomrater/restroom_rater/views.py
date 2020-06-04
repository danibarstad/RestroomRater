# import requests
from django.shortcuts import render, redirect, get_object_or_404
from . import yelp_api
from .models import Venue
from .forms import RestroomForm


def homepage(request):
    return render(request, 'restroom_rater/homepage.html')


def venue_list(request):
    search_zip = request.GET.get('zip_code')

    if not Venue.objects.filter(zip_code=search_zip).exists():
        venues = yelp_api.get_name(search_zip)
        venues = Venue.objects.filter(zip_code=search_zip).order_by('name')
    else:
        venues = Venue.objects.filter(zip_code=search_zip).order_by('name')

    return render(request, 'restroom_rater/venue_list.html', { 'venues': venues, 'search_zip': search_zip})


def venue_detail(request, venue_pk):
    venue = get_object_or_404(Venue, pk=venue_pk)
    restroom_form = RestroomForm()
    return render(request, 'restroom_rater/venue_detail.html', {'venue': venue, 'restroom_form': restroom_form})


def venue_restroom(request, venue_pk):
    restroom_form = RestroomForm()
    venue = get_object_or_404(Venue, pk=venue_pk)
    
    return render(request, 'restroom_rater/venue_detail.html', { 'restroom_form': restroom_form, 'venue': venue })