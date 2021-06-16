from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import TestimonialForm


def all_testimonials(request):
    """ A view to show all testimonials """

    testimonials = Testimonial.objects.all()
    
    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)


