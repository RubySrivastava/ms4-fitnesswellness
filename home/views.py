from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .models import Testimonial


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def all_testimonials(request):
    """ A view to show all testimonials """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'home/index.html', context)