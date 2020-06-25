from django.urls import path
from . import views, views_users, views_venues
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homepage, name='homepage'),

    # Venue
    path('venues/list/', views_venues.venue_list, name='venue_list'),
    path('venues/detail/<int:venue_pk>/', views_venues.venue_detail, name='venue_detail'),

    # Review
    path('reviews/detail/<int:review_pk>/',views.review_detail, name='review_detail'),
    
    # User
    path('user/profile/<int:user_pk>/', views_users.user_profile, name='user_profile'),
    path('user/profile/edit', views_users.edit_user_profile, name='edit_user_profile'),
    path('user/profile/', views_users.my_user_profile, name='my_user_profile'),
    path('user/profile/password/', views_users.change_password, name='change_password'),

    # Register
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views_users.register, name='register'),

    # Breadcrumbs
    path('breadcrumbs/', views.breadcrumbs, name='breadcrumbs')
]