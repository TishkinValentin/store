from django.shortcuts import render
from products.models import *


def index(request):
    context = {
        'title': 'store'
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'store',
        'categories': ProductCategory.objects.all(),
        'products': Products.objects.all()
    }
    return render(request, 'products/products.html', context=context)
