from django.shortcuts import render

# Create your views here.
def membership(request):
    """ A view to return our gym page"""

    return render(request, 'membership/membership.html')