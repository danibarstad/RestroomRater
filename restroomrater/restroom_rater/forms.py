from django import forms
from .models import ZipCode

class NewZipCodeForm(forms.ModelForm):
    class Meta:
        model = ZipCode
        fields = ('zipCode',)