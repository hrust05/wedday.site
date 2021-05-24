from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        label_suffix='',
        help_text='Введите имя вашего профиля на сайте', )
    email = forms.EmailField(
        label='Адрес электронной почты',
        label_suffix='',
        help_text='Укажите адрес электронной почты', )
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

# class ProfileRegistrationForm(UserCreationForm):
#     phone_number = forms.CharField()
#     email = forms.EmailField()
#     birth_date = forms.DateField()
#     location = forms.CharField()
#
#     class Meta:
#         model = User
#         fields = ('username', 'phone_number', 'email', 'birth_date', 'location', 'password1', 'password2')

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         # fields = ('first_name', 'last_name', 'email')
#         fields = '__all__'
#
#
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         # fields = ('url', 'location', 'company')
#         fields = '__all__'
