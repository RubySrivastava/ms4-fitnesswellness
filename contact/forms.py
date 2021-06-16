from django import forms
from django.contrib.auth.forms import UserCreationForm

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('email','user','testimonial')