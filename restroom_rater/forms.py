from django import forms
from .models import RestroomReview

from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# form to search zip code
class SearchForm(forms.Form):
    zip_code = forms.CharField(required=True, label='Zip Code', max_length=5)


# form to review restroom
class RestroomForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    comment = forms.SlugField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave your review here'}))

    class Meta:
        model = RestroomReview
        fields = (
            'user', 'public', 'rest_type', 
            'baby', 'needle', 'handicap', 
            'rating', 'title', 'comment'
            )