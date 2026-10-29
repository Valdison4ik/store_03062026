from django.db import models
from .categories import Category
from .suppliers import Supplier


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория'
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name='products', verbose_name='Поставщик'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')
    article = models.CharField(max_length=50, unique=True, verbose_name='Артикул')
    available = models.BooleanField(default=True, verbose_name='В наличии')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.article})'
