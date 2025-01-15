from django.shortcuts import render, HttpResponseRedirect
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


def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    basket_item = Basket.objects.filter(user=request.user, product=product)
    if basket_item.exists():
        basket = basket_item.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    else:
        basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))