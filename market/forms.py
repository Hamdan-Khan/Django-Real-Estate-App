from django import forms
from social.models import Message


class PropertyContactForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ["sent_at", "sender", "receiver"]
