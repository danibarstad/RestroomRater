from django import forms
from .models import Result, Establishment

class NewResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('city',)