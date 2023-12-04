from django.db import models
from users.models import User


class ProductsCategory(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=64)
    description = models.CharField(verbose_name='Описание', max_length=256, blank=True)

    class Meta:
        verbose_name = 'Категорbя'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=64)
    short_descroption = models.CharField(verbose_name='Краткое описание', max_length=150, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    category = models.ForeignKey(ProductsCategory, verbose_name='Категория', on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name='Цена', max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
    image = models.ImageField(verbose_name='Изображение', upload_to='product_images')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Список товаров'

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Покупатель {self.user.username} |  Товар {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price