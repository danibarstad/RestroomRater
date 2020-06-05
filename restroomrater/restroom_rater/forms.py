from django import forms
from .models import RestroomReview


class SearchZipForm(forms.Form):
    zip_code = forms.CharField(required=True, label='Zip Code', max_length=5)


class RestroomForm(forms.ModelForm):
    class Meta:
        model = RestroomReview
        fields = (
            'public', 'number', 'rest_type', 'baby', 'needle', 
            'handicap', 'rating', 'title', 'comment'
            )


# class RestroomReviewForm(forms.Form):
#     MEN = 'M'
#     WOMEN = 'W'
#     UNISEX = 'U'
#     FAMILY = 'F'
#     RESTROOM_TYPE_CHOICES = [
#         (MEN, 'Men'),
#         (WOMEN, 'Women'),
#         (UNISEX, 'Unisex'),
#         (FAMILY, 'Family')
#     ]
#     public_private = forms.BooleanField(required=False, label='Public')
#     number = forms.IntegerField(required=False, label='How Many', min_value=0)
#     restoom_type = forms.ChoiceField(required=False, label='Type', choices=RESTROOM_TYPE_CHOICES)
#     baby = forms.BooleanField(required=False, label='Changing Table')
#     needle = forms.BooleanField(required=False, label='Needle Box')
#     handicap = forms.BooleanField(required=False, label='Handicap Accessible')
#     title = forms.CharField(required=True, label='Title')