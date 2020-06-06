from django import forms
from .models import RestroomReview


class SearchZipForm(forms.Form):
    zip_code = forms.CharField(required=True, label='Zip Code', max_length=5)


class RestroomForm(forms.ModelForm):
    class Meta:
        model = RestroomReview
        fields = (
            'public', 'rest_type', 'baby', 'needle', 
            'handicap', 'rating', 'title', 'comment'
            )