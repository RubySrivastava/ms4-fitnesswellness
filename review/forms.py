from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'