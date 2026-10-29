from rest_framework.serializers import ModelSerializer, ValidationError
from .orders import OrderSerializer
from .products import ProductSerializer
from store.models import OrderItem

MAX_QUANTITY = 1000


class OrderItemSerializer(ModelSerializer):
    order = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price']


class OrderItemCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price']

    def validate_quantity(self, value: int) -> int:
        if value > MAX_QUANTITY:
            raise ValidationError(f'The quantity should by less than or equal to {MAX_QUANTITY}.')

        return value
