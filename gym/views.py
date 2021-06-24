from django.shortcuts import render


def ourgym(request):
    """ A view to return our gym page"""

    return render(request, 'gym/ourgym.html')
