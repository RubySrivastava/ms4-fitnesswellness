from django.shortcuts import render, reverse
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
    

def add_testimonial(request):
    """ Add a testimony """

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save()
            messages.success(request, 'Successfully added testimony!')
            return redirect(reverse('testimonial'))
        else:
            messages.error(request, 'Failed to add testimony. Please ensure the form is valid.')
    else:
        form = TestimonialForm()
        
    template = 'testimonials/testimonials.html'
    context = {
        'form': form,
    }

    return render(request, template, context)