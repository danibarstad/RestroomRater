from django import forms


class SearchZipForm(forms.Form):
    zip_code = forms.CharField(required=True, label='Zip Code', max_length=5)


class RestroomForm(forms.Form):
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
    public_private = forms.BooleanField(required=True, label='Public')
    number = forms.IntegerField(required=True, label='How Many', min_value=0)
    restoom_type = forms.ChoiceField(required=True, label='Type', choices=RESTROOM_TYPE_CHOICES)