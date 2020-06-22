from .forms import RestroomForm
from django.utils import timezone
from .models import Venue, RestroomReview
from django.shortcuts import render, redirect, get_object_or_404


def homepage(request):
    return render(request, 'restroom_rater/homepage.html')


def review_detail(request, review_pk):
    review = get_object_or_404(RestroomReview, pk=review_pk)
    return render(request, 'restroom_rater/review_detail.html', {'review': review})

def breadcrumbs(request):
    return render(request, 'restroom_rater/breadcrumbs.html')