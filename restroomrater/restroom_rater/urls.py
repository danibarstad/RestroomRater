from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('venues/list/', views.venue_list, name='venue_list'),
    path('venues/detail/<int:venue_pk>/', views.venue_detail, name='venue_detail'),
    path('venues/restroom/', views.venue_restroom, name='venue_restroom')
]