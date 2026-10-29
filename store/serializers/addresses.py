from rest_framework.serializers import ModelSerializer
from store.models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
