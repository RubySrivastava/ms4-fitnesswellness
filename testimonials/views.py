from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .models import Testimonial
from .forms import TestimonialForm


def all_testimonials(request):
    """ A view to show all testimonials """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)
    

def add_testimonial(request, template='testimonials/testimonial_form.html'):
    """ Add a testimony """

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added testimony!')
        else:
            messages.error(request, 'Failed to add testimony.')
    else:
        form = TestimonialForm()
        
    template = 'testimonials/testimonial_form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)