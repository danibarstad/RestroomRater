from . import yelp_api
from .forms import RestroomForm
from django.utils import timezone
from .models import RestroomReview, Venue
from django.shortcuts import get_object_or_404, redirect, render


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
    reviews = RestroomReview.objects.filter(venue=venue_pk)

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

    return render(request, 'restroom_rater/venue_detail.html', {'venue': venue, 'restroom_form': restroom_form, 'reviews': reviews})