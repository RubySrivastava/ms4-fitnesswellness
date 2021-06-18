from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .models import Review
from .forms import ReviewForm


def all_reviews(request):
    """ A view to show all reviews """

    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)
    

def add_review(request, template='reviews/review_form.html'):
    """ Add a review """

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review!')
        else:
            messages.error(request, 'Failed to add review.')
    else:
        form = ReviewForm()
        
    template = 'reviews/review_form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)