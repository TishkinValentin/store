from django.db import models
from users.models import *


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name='Наименование', blank=False)
    description = models.CharField(max_length=128, verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование', blank=False)
    short_description = models.CharField(max_length=512, verbose_name='Краткое описание', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    category = models.ForeignKey(ProductCategory, verbose_name='Категория', blank=False, on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Изображение', upload_to='Products_images', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость', blank=False)
    quantity = models.PositiveIntegerField(verbose_name='Количество', blank=True)

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Номенклатура'

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    create_datastamp = models.DateTimeField(verbose_name='Добавлено', auto_now_add=True)

    class Meta:
        verbose_name = 'Карзина'
        verbose_name_plural = 'Карзина'

    def __str__(self):
        return f'{self.user.username} | {self.product.name} | {self.quantity}'

    def sum(self):
        return self.quantity * self.product.price
