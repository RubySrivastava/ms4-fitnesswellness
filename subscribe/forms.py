from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Subscribe  

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email',)

