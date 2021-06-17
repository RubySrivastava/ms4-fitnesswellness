from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'