# import requests
from django.shortcuts import render, redirect, get_object_or_404
from .forms import get_zip
from . import yelp_api
from .models import Establishment

# Create your views here.

def homepage(request):
    new_zip_form = get_zip()
    search_zip = request.GET.get('zip_code')

    venues = yelp_api.get_name(search_zip)

    return render(request, 'restroom_rater/homepage.html', { 'venues': venues, 'new_zip_form': new_zip_form})


def venue_detail(request, venue_pk):
    venue = get_object_or_404(Establishment, pk=venue_pk)
    return render(request, 'venue_detail.html', {'venue': venue})