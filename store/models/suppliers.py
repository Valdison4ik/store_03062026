from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    contact_email = models.EmailField(verbose_name='Email для связи')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')

    class Meta:
        db_table = 'supplier'
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['name']

    def __str__(self):
        return self.name
