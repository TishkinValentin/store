from django.contrib import admin
from products.models import *


@admin.register(ProductsCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
