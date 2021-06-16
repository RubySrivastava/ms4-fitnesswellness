from django.shortcuts import render
from .models import Testimonial

# Create your views here.

def all_testimonials(request):
    """ A view to show all testimonials """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)