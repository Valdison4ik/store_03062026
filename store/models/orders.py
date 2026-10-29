from django.db import models
from .customers import Customer


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='orders', verbose_name='Клиент'
    )
    order_date = models.DateTimeField(verbose_name='Дата заказа')

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-order_date']

    def __str__(self):
        return f'Заказ №{self.pk} от {self.customer}'
