from django.contrib import admin
from .models import Establishment, Restroom, Review

# Register your models here.

admin.site.register(Establishment)
admin.site.register(Restroom)
admin.site.register(Review)