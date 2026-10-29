from django.db import models
from .orders import Order
from .products import Product


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='order_items', verbose_name='Товар'
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
        ordering = ['order']

    def __str__(self):
        return f'{self.product} x{self.quantity}'
