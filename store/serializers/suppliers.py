from rest_framework.serializers import ModelSerializer
from store.models import Supplier


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
