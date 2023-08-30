from .models import CustomUser, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from market.models import Property
from social.models import Message


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'gender', 'password1', 'password2']


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact_number', 'profile_pic',
                  'first_name', 'last_name', 'city', 'description']


class AddPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ["added_at", "owner"]


class ProfileContactForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ["sent_at", "sender", "receiver", "property"]
