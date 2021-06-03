from django.shortcuts import render

# Create your views here.

def ourgym(request):
    """ A view to return our gym page"""

    return render(request, 'gym/ourgym.html')