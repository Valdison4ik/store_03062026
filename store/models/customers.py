from django.db import models
from .addresses import Address


class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='customers', verbose_name='Адрес'
    )
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')

    # deleted, deleted_at

    class Meta:
        db_table = 'customer'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['last_name', 'first_name']

    @property
    def deleted(self) -> bool:
        return True if self.deleted_at else False

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
