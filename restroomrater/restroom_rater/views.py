import requests
from django.shortcuts import render
from .forms import get_zip

# Create your views here.

def homepage(request):
    # zipCodes = ZipCode.objects.all()
    new_zip_form = get_zip()
    return render(request, 'restroom_rater/homepage.html', { 'new_zip_form': new_zip_form})