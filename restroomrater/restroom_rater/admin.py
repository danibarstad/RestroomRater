from django.contrib import admin
from .models import Venue, Restroom, Review

# Register your models here.

admin.site.register(Venue)
admin.site.register(Restroom)
admin.site.register(Review)