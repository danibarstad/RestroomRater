from django import forms
from .models import ZipCode

class NewZipCodeForm(forms.ModelForm):
    class Meta:
        model = ZipCode
        fields = ('zipCode',)

class get_zip(forms.TextInput):
    class Meta:
        fields = ('zip_code',)