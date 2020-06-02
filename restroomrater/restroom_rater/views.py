import requests
from django.shortcuts import render
from .forms import get_zip
from . import yelp_api

# Create your views here.

def homepage(request):
    # zipCodes = ZipCode.objects.all()
    new_zip_form = get_zip()
    search_zip = request.GET.get('zip_code')

    establishments = yelp_api.get_name(search_zip)

    return render(request, 'restroom_rater/homepage.html', { 'establishments': establishments, 'new_zip_form': new_zip_form})