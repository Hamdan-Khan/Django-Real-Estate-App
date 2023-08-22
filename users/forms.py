from .models import CustomUser, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from market.models import Property, Location


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'gender', 'password1', 'password2']


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ['email',]


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact_number', 'profile_pic',
                  'first_name', 'last_name', 'city']


class AddPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ["added_at",]
