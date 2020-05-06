from django import forms

class get_zip(forms.Form):
    zip_code = forms.CharField(required=True, label='Zip Code', max_length=5)