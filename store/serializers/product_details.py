from rest_framework.serializers import ModelSerializer
from .products import ProductSerializer
from store.models import ProductDetail


class ProductDetailSerializer(ModelSerializer):
    product = ProductSerializer(required=True)

    class Meta:
        model = ProductDetail
        fields = ('id', 'product', 'description', 'manufacturing_date', 'expiration_date', 'weight')
        # '__all__'


class ProductDetailCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'
