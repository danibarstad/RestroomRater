from django import forms
from .models import RestroomReview

from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# form to search zip code
class SearchForm(forms.Form):
    zip_code = forms.CharField(required=True, label='Zip Code', max_length=5)


# form to review restroom
class RestroomForm(forms.ModelForm):
    class Meta:
        model = RestroomReview
        fields = (
            'public', 'rest_type', 'baby', 'needle', 
            'handicap', 'rating', 'title', 'comment'
            )


# form for user to register
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        def clean_username(self):
            username = self.cleaned_data['username']
            if not username:
                raise ValidationError('Please enter a username')
            if User.objects.filter(username__iexact=username).exists():
                raise ValidationError('A user with that username already exists')
            return username
        
        def clean_first_name(self):
            first_name = self.cleaned_data['first_name']
            if not first_name:
                raise ValidationError('Please enter your first name')
            return first_name
        
        def clean_last_name(self):
            last_name = self.cleaned_data['last_name']
            if not last_name:
                raise ValidationError('Please enter your last name')
            return last_name
        
        def clean_email(self):
            email = self.cleaned_data['email']
            if not email:
                raise ValidationError('Please enter an email address')
            if User.objects.filter(email__iexact=email).exists():
                raise ValidationError('A user with that email address already exists')
            return email
        
        def save(self, commit=True):
            user = super(UserRegistrationForm, self).save(commit=False)
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
            return user


# form for user to edit profile
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
    def save(self, commit=True):
        user= super(EditProfileForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user