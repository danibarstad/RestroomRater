from django.db import models
import datetime

# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=2, blank=False)    # What about international?

    def __str__(self):
        return f'Venue name: {self.name} in {self.city}, {self.state}'


class Restroom(models.Model):
    MEN = 'M'
    WOMEN = 'W'
    UNISEX = 'U'
    FAMILY = 'F'
    RESTROOM_TYPE_CHOICES = [
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (UNISEX, 'Unisex'),
        (FAMILY, 'Family')
    ]
    name = models.ForeignKey(Venue, blank=False, on_delete=models.CASCADE)
    public = models.BooleanField(blank=False)
    number = models.IntegerField()
    rest_type = models.CharField(
        max_length=1, 
        choices=RESTROOM_TYPE_CHOICES, 
        default=MEN
    )
    baby = models.BooleanField()
    needle = models.BooleanField()
    handicap = models.BooleanField()

    def __str__(self):
        return f"""Restroom at {self.name} Public: {self.public}
                    How Many?: {self.number} Type: {self.rest_type}
                    Changing Table: {self.baby} Needle Disposal: {self.needle} 
                    Handicap Accessible: {self.handicap}"""


class Review(models.Model):
    venue = models.ForeignKey(Venue, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField()
    title = models.CharField(max_length=200, blank=False)
    comment = models.TextField(max_length=1000, blank=False)
    posted_date = models.DateTimeField(blank=False)

    def publish(self):
        posted_date = datetime.datetime.today()
        self.save()
    
    def __str__(self):
        return f'Review for user ID {self.user} for establishment ID {self.venue} with rating {self.rating} title {self.title} review {self.comment} posted on {self.posted_date}'
        # return 'Review for user ID {} for establishment ID {} with title {} review {} posted on {}'.format(self.user, self.establishment, self.title, self.comment, self.posted_date)