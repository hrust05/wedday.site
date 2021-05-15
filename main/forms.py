from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField
    email = forms.EmailField(max_length=254, required=False)
    birth_date = forms.DateField()
    location = forms.CharField

    class Meta:
        model = User
        fields = ('username', 'email', 'birth_date', 'password1', 'password2',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ('first_name', 'last_name', 'email')
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ('url', 'location', 'company')
        fields = '__all__'
