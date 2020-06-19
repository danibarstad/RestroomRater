import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

User._meta.get_field('email')._unique = True
User._meta.get_field('username')._unique = True

User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False


class Venue(models.Model):
    name = models.CharField(max_length=200, blank=False)
    category = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=2, blank=False)    # What about international?
    zip_code = models.CharField(max_length=200, blank=False)
    image = models.CharField(max_length=200)

    def __str__(self):
        return f'Venue name: {self.name} in {self.city}, {self.state} {self.zip_code}'


class RestroomReview(models.Model):
    MEN = 'M'
    WOMEN = 'W'
    UNISEX = 'U'
    FAMILY = 'F'
    RESTROOM_TYPE_CHOICES = [
        ('M', 'Men'),
        ('W', 'Women'),
        ('U', 'Unisex'),
        ('F', 'Family')
    ]
    RATING_CHOICES = [
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    ]
    venue = models.ForeignKey(Venue, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', blank=False, on_delete=models.CASCADE)
    public = models.BooleanField(blank=False)
    rest_type = models.CharField(
        max_length=1, 
        choices=RESTROOM_TYPE_CHOICES, 
        default=MEN
    )
    baby = models.BooleanField('Changing Table')
    needle = models.BooleanField('Sharps Container')
    handicap = models.BooleanField('Handicap Accessible')
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    title = models.CharField(max_length=200, blank=False)
    comment = models.TextField(max_length=1000, blank=False)
    posted_date = models.DateTimeField(blank=False)

    def publish(self):
        posted_date = datetime.datetime.today()
        self.save()
    
    def __str__(self):
        return f'Review for {self.venue.name} by {self.user}'