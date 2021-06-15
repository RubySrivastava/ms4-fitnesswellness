from django.contrib import admin

from django.urls import path
from . import views
admin.autodiscover()


urlpatterns = [
    path('', views.subscribe, name='subscribe'),
]