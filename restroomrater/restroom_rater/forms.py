from django import forms


class SearchZipForm(forms.Form):
    zip_code = forms.CharField(required=True, label='Zip Code', max_length=5)