from rest_framework.serializers import ModelSerializer
from .categories import CategorySerializer
from .suppliers import SupplierSerializer
from store.models import Product


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'supplier', 'price', 'quantity', 'article', 'available']
        # '__all__'


class ProductCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
