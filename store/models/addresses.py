from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house = models.CharField(max_length=10, verbose_name='Дом')

    class Meta:
        db_table = 'address'
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['country', 'city']

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street} {self.house}'
