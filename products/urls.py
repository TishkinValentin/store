from django.contrib import admin
from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:category_id>/', products, name='product_category'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-del/<int:product_id>/', basket_delete, name='basket_delete')
]