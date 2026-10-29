from rest_framework.serializers import ModelSerializer
from .customers import CustomerSerializer
from store.models import Order


class OrderSerializer(ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_date']
        read_only_fields = ['order_date']
        # '__all__'


class OrderCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer']
        read_only_fields = ['order_date']
