from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import SubscriberForm


def subscribe(request, template='subscribe/subscribe.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Unpack form values
            email = form.cleaned_data['email']
            # Create the User record
            user = User(email=email)
            user.save()     
    else:
        form = SubscriberForm()

    return render(request, template, {'form':form})