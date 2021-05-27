from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SiteUser, Profile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = SiteUser
        fields = [
            'username',
            'location',
            'birth_date',
            'first_name',
            'last_name',
            'phone_number',
            'description',
            'email',
            'password1',
            'password2',
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = [
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'birth_date',
            'location',
            'description',
        ]


class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()
