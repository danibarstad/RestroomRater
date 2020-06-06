from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('venues/list/', views.venue_list, name='venue_list'),
    path('venues/detail/<int:venue_pk>/', views.venue_detail, name='venue_detail'),

    path('reviews/detail/<int:review_pk>/',views.review_detail, name='review_detail')
]