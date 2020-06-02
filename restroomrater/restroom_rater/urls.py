from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('venues/detail/<int:venue_pk>/', views.venue_detail, name='venue_detail')
]