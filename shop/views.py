from django.shortcuts import render
from .models import Product

# Create your views here.

def shop_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'shop/shop.html', context)