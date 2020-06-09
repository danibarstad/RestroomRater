from . import yelp_api
from .forms import RestroomForm
from django.utils import timezone
from .models import Venue, RestroomReview
from django.shortcuts import render, redirect, get_object_or_404


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

    if request.method == 'POST':
        restroom_form = RestroomForm(request.POST, request.FILES, instance=None)
        if restroom_form.is_valid():
            review = restroom_form.save(commit=False)
            review.user = request.user
            review.venue = venue
            review.posted_date = timezone.now()
            review.save()
            return redirect('review_detail', review_pk=review.pk)
    else:
        restroom_form = RestroomForm()

    return render(request, 'restroom_rater/venue_detail.html', {'venue': venue, 'restroom_form': restroom_form})


def review_detail(request, review_pk):
    review = get_object_or_404(RestroomReview, pk=review_pk)
    return render(request, 'restroom_rater/review_detail.html', {'review': review})