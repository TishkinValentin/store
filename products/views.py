from django.shortcuts import render, HttpResponseRedirect
from products.models import *
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'products/index.html')

def products(request, category_id=None):
    content = {'title': 'Geek goods',
               'categories': ProductsCategory.objects.all()}
    if category_id==None:
        content.update({'products': Product.objects.all()})
    else:
        content.update({'products': Product.objects.filter(category_id=category_id)})
    return render(request, 'products/products.html', context=content)

@login_required()
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket:
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required()
def basket_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    if basket.quantity == 1:
        basket.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket.quantity -= 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))