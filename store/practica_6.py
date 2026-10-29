import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# import calendar
# from datetime import date
from django.utils import timezone
from django.db.models import Avg, Sum, Min, Max, F, Count, ExpressionWrapper, fields
from store.models import Product, ProductDetail, Category, Order, OrderItem, Customer, Supplier, Address

# Агрегация

"""
Задача 1
Общая стоимость всех продуктов
Цель: Вычислить общую стоимость всех продуктов в базе данных.
Инструкция:
1. Используйте модель Product.
2. Рассчитайте общую стоимость всех продуктов (цена умноженная на количество) в базе данных.
"""

# total_value = Product.objects.aggregate(total_value=Sum(F('price') * F('quantity')))
# # print(total_value)
# print(f"Общая стоимость всех продуктов: {total_value['total_value']}")

"""
Задача 2
Средняя цена продуктов по категориям
Цель: Вычислить среднюю цену продуктов для каждой категории.
Инструкция:
1. Используйте модели Product и Category.
2. Группируйте продукты по категориям и вычислите среднюю цену для каждой категории.
"""
# average_price_by_category = Product.objects.values('category__name').annotate(
#     average_price=Avg('price')).order_by('-price')
#
# print(average_price_by_category)
#
# for entry in average_price_by_category:
#     print(f"Категория: {entry['category__name']}, Средняя цена:{entry['average_price']}")

"""
Задача 3
Самый дешевый и самый дорогой продукт
Цель: Найти самый дешевый и самый дорогой продукт.
Инструкция:
1. Используйте модель Product.
2. Найдите продукт с минимальной ценой и продукт с максимальной ценой.
"""

# cheapest_product = Product.objects.aggregate(min_price=Min('price'))['min_price']
# most_expensive_product = Product.objects.aggregate(max_price=Max('price'))['max_price']
#
# print(f"Самый дешевый продукт: {cheapest_product}")
# print(f"Самый дорогой продукт: {most_expensive_product}")

"""
Задача 4
Заказы
Цель: Вычислить количество заказов и общую стоимость заказов для каждого клиента.
Инструкция:
1. Используйте модели Order, OrderItem, и Customer.
2. Группируйте по клиентам и вычислите количество заказов и общую стоимость заказов для каждого клиента.
"""
# total_order = Order.objects.aggregate(order_cnt=Count('id'))['order_cnt']
# print(f'Общее количество заказов: {total_order}')
#
# orders_summary_by_customer = Order.objects.values('customer__first_name','customer__last_name').annotate(
#     order_count=Count('id'),
#     total_spent=Sum(F('items__quantity')*F('items__price'))).order_by('customer__last_name')
#
# # print(orders_summary_by_customer)
#
# for entry in orders_summary_by_customer:
#     print(f"Клиент: {entry['customer__first_name']} {entry['customer__last_name']}, Заказов:"
#           f"{entry['order_count']}, Общая сумма: {entry['total_spent']}")

"""
Задача 5
Общий вес продуктов по категориям
Цель: Рассчитать общий вес всех продуктов для каждой категории.
Инструкция:
1. Используйте модели Product, ProductDetail, и Category.
2. Группируйте по категориям и вычислите общий вес всех продуктов в каждой категории.
"""

# total_weight_by_category = Product.objects.values('category__name').annotate(
#     total_weight=Sum('detail__weight')).order_by('-total_weight')
#
# for entry in total_weight_by_category:
#     print(f"Категория: {entry['category__name']}, Общий вес: {entry['total_weight']}")

"""
Задача 6
Количество продуктов у поставщиков
Цель: Вычислить количество различных продуктов, которые поставляет каждый поставщик.
Инструкция:
1. Используйте модели Product и Supplier.
2. Группируйте продукты по поставщикам и подсчитайте количество продуктов для каждого поставщика.
"""
#
# products_count_by_supplier = Product.objects.values('supplier__name').annotate(
#     product_count=Count('id')).order_by('-product_count')
#
# for entry in products_count_by_supplier:
#     print(f"Поставщик: {entry['supplier__name']}, Количество продуктов: {entry['product_count']}")
#
"""
Задача 7
Средняя продолжительность жизни продуктов
Цель: Вычислить среднюю продолжительность жизни продуктов (в днях) на основе даты производства и
срока годности.
Инструкция:
1. Используйте модели Product и ProductDetail.
2. Рассчитайте среднее время от даты производства до срока годности для всех продуктов.
"""

# average_lifetime = ProductDetail.objects.annotate(lifetime=ExpressionWrapper(
#                                                   F('expiration_date') - F('manufacturing_date'),
#     output_field=fields.DurationField())).aggregate(average_lifetime=Avg('lifetime'))
# # ['average_lifetime']
#
# print(average_lifetime)
#
# print(f"Средняя продолжительность жизни продуктов: {average_lifetime['average_lifetime'].days} дней")

"""
Задача 8
Общая сумма заказов для каждого клиента
Цель: Рассчитать общую сумму всех заказов для каждого клиента.
Инструкция:
1. Используйте модели OrderItem, Order, и Customer.
2. Группируйте заказы по клиентам и вычислите общую сумму заказов для каждого клиента.
"""
#
# total_spent_by_customer  = Order.objects.values('customer__first_name','customer__last_name').annotate(
#     total_spent=Sum(F('items__price')*F('items__quantity'))).order_by('-total_spent')
#
# print(total_spent_by_customer)
#
# for entry in total_spent_by_customer:
#     print(f"Клиент: {entry['customer__first_name']} {entry['customer__last_name']}, "
#           f"Общая сумма заказов: {entry['total_spent']}")


# Order_by

"""
Задача 1
Сортировка продуктов по цене
Цель: Сортировать список продуктов по их цене в порядке убывания.
Инструкция:
1. Используйте модель Product.
2. Получите список продуктов, отсортированных по цене в порядке убывания.
"""
#
# products_descending = Product.objects.values('name', 'price').order_by('-price')
# print(products_descending)
#
# print("Продукты по убыванию цены:")
# for product in products_descending:
#     print(product)
#     print(f"{product['name']}: {product['price']}")
#
#
# products_descending = Product.objects.order_by('-price')
# print(products_descending)
#
# print("Продукты по убыванию цены:")
# for product in products_descending:
#     print(product)
#     print(f"{product.name}: {product.price}, {product.quantity} шт.")

"""
Задача 2
Цель: Сортировать список заказов по их общей стоимости.
Инструкция:
1. Используйте модели Order и OrderItem.
2. Получите список заказов, отсортированных по их общей стоимости в порядке убывания.
"""
# orders_by_total  = (Order.objects.annotate(total_amount=Sum(F('items__price')*F('items__quantity'))).
#                     order_by('-total_amount'))
# print(orders_by_total)
#
# print("Заказы по общей стоимости:")
# for order in orders_by_total:
#     # print(order)
#     print(f"Заказ {order.id}, Общая стоимость: {order.total_amount}")

"""
Задача 3
Сортировка адресов по стране и городу
Цель: Отсортировать список адресов сначала по стране, затем по городу.
Инструкция:
1. Используйте модель Address.
2. Получите список адресов, отсортированных по стране и затем по городу в алфавитном порядке.
"""
# order_addresses = Address.objects.order_by('country','city')
#
# print("Адреса по стране и городу:")
# for adr in order_addresses:
#     print(adr.country, adr.city, adr.street)

"""
Задача 4
Сортировка заказов по количеству позиций заказа
Цель: Отсортировать список заказов по количеству позиций в каждом заказе.
Инструкция:
1. Используйте модели Order и OrderItem.
2. Получите список заказов, отсортированных по количеству позиций в каждом заказе.
"""

# sorted_orders = Order.objects.annotate(total=Sum('items__quantity')).order_by('total')
#
# for ord in sorted_orders:
#     print(f'{ord.id} - {ord.total} единиц товаров')


# sorted_orders = Order.objects.annotate(total=Count('items__id')).order_by('total')
#
# print("Заказы по количеству позиций:")
# for ord in sorted_orders:
#     print(f'{ord.id} - {ord.total} позиций')


# Временные метки
"""
Задача
Заказы за последний месяц
Цель: Найти все заказы, сделанные за последний месяц.
Инструкция:
1. Используйте модель Order.
2. Используйте фильтр для поиска заказов, сделанных в последний месяц от текущей даты.
"""

# # Дата один месяц назад
# one_month_ago = timezone.now() - timezone.timedelta(days=30)
#
# print(one_month_ago)
#
# # Заказы за последний месяц
# recent_orders = Order.objects.filter(order_date__gte=one_month_ago).order_by('order_date')
#
# print(recent_orders)
#
# print("Заказы за последний месяц:")
# for order in recent_orders:
#     print(f"Заказ {order.id}, Дата: {order.order_date}")
#
# print('*' * 90)
#
# # Получаем текущую дату и время с учетом настроек проекта
# now = timezone.now()
#
# # Фильтруем записи, у которых год и месяц совпадают с текущими
# current_month_records = Order.objects.filter(order_date__year=now.year, order_date__month=now.month).order_by('order_date')
#
# print("Заказы за текущий месяц:")
# for order in current_month_records:
#     print(f"Заказ {order.id}, Дата: {order.order_date}")


# Срезы

"""
Задача 1
Первые 5 продуктов
Цель: Извлечь первые 5 продуктов из списка всех продуктов.
Инструкция:
1. Используйте модель Product.
2. Используйте срез для получения первых 5 продуктов.
"""
#
# first_five_products = Product.objects.all()[:5]
#
# print("Первые 5 продуктов:")
# for product in first_five_products:
#     print(f"{product.name}: {product.price}")

"""
Задача 2
Самые дорогие продукты
Цель: Найти 10 самых дорогих продуктов.
Инструкция:
1. Используйте модель Product.
2. Используйте order_by для сортировки продуктов по цене в порядке убывания.
3. Используйте срез для получения первых 10 записей.
"""
top_ten_expensive_products = Product.objects.order_by('-price', '-name')

print(top_ten_expensive_products)

print("10 самых дорогих продуктов:")
for product in top_ten_expensive_products[:10]:
    print(f"{product.name}: {product.price}")
print('*' * 90)

top_ten_expensive_products = Product.objects.order_by('-price', '-name')[:10:1]

print(top_ten_expensive_products)

print("10 самых дорогих продуктов:")
for product in top_ten_expensive_products:
    print(f"{product.name}: {product.price}")