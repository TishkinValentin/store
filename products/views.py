from django.shortcuts import render
from products.models import *


def index(request):
    return render(request, 'products/index.html')


def products(request):
    content = {'title': 'Geek goods',
               'categories': ProductsCategory.objects.all(),
               'products': Product.objects.all()}
    return render(request, 'products/products.html', context=content)
