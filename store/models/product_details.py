from django.db import models
from .products import Product


class ProductDetail(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name='detail', verbose_name='Товар'
    )
    description = models.TextField(verbose_name='Описание')
    manufacturing_date = models.DateField(verbose_name='Дата изготовления')
    expiration_date = models.DateField(null=True, blank=True, verbose_name='Срок годности')
    weight = models.DecimalField(max_digits=8, decimal_places=3, verbose_name='Вес, кг')

    class Meta:
        db_table = 'product_detail'
        verbose_name = 'Характеристики товара'
        verbose_name_plural = 'Характеристики товаров'
        ordering = ['product']

    def __str__(self):
        return f'Детали товара: {self.product}'
