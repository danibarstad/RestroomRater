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
    public_private = forms.BooleanField(required=False, label='Public')
    number = forms.IntegerField(required=False, label='How Many', min_value=0)
    restoom_type = forms.ChoiceField(required=False, label='Type', choices=RESTROOM_TYPE_CHOICES)
    baby = forms.BooleanField(required=False, label='Changing Table')
    needle = forms.BooleanField(required=False, label='Needle Box')
    handicap = forms.BooleanField(required=False, label='Handicap Accessible')