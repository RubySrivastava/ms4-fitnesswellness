from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Subscribe  

class SubscriberForm(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )