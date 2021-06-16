from django import forms
from django.contrib.auth.forms import UserCreationForm

class TestimonialForm(forms.ModelForm):
    class Meta:
        fields = ('email', 'name', 'testimony')