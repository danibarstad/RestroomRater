from django.shortcuts import render
from .models import ZipCode
from .forms import NewZipCodeForm

# Create your views here.

def homepage(request):
    # zipCodes = ZipCode.objects.all()
    new_zip_form = NewZipCodeForm()
    return render(request, 'restroom_rater/homepage.html', { 'new_zip_form': new_zip_form})