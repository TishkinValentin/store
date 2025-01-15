from django.shortcuts import render
from products.models import *
from django.core.paginator import Paginator


def index(request):
    context = {
        'title': 'store'
    }
    return render(request, 'products/index.html', context=context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'store',
        'categories': ProductCategory.objects.all()
    }
    if category_id:
        products_item = Products.objects.filter(category_id=category_id)
    else:
        products_item = Products.objects.all()
    paginator = Paginator(products_item, 3)
    products = paginator.get_page(page)
    context.update({'products': products})
    return render(request, 'products/products.html', context=context)
