from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='reviews'),
    path('reviews/', views.add_review, name='add_review'),
]