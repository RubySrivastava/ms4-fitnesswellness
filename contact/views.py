from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import TestimonialForm


def add_testimonial(request, template='contact/contact.html'):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added testimonial!')
        else:
            messages.error(request, 'Failed to add testimonial')
    else:
        form = TestimonialForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
    