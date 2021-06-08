from django.shortcuts import render

# Create your views here.


def subscribe(request):
    """ A view to return the index page """

    return render(request, 'subscribe/subscribe.html')