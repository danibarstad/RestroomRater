from django.urls import path
from . import views, views_venues
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.homepage, name='homepage'),

    # Venue
    path('venues/list/', views_venues.venue_list, name='venue_list'),
    path('venues/detail/<int:venue_pk>/', views_venues.venue_detail, name='venue_detail'),

    # Review
    path('reviews/detail/<int:review_pk>/',views.review_detail, name='review_detail'),

    # Breadcrumbs
    path('breadcrumbs/', views.breadcrumbs, name='breadcrumbs'),

    # Favicon
    # path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]