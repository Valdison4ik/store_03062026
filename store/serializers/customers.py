from rest_framework.serializers import ModelSerializer, ValidationError
from .addresses import AddressSerializer
from store.models import Customer


# import re

class CustomerSerializer(ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['id'
            , 'first_name'
            , 'last_name'
            , 'email'
            , 'phone_number'
            , 'address'
            , 'date_joined'
            , 'deleted'
            , 'deleted_at']
        read_only_fields = ['id', 'date_joined', 'deleted', 'deleted_at']


class CustomerCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

    def validate_phone_number(self, value: str) -> str:
        """номер телефона состоит из 10-15 цифр и не содержит букв или специальных символов"""
        if not value.isdigit():
            raise ValidationError("The phone number should contain only digits.")

        l = len(value)
        if l < 10 or l > 15:
            raise ValidationError("The length of phone number should be between 10 and 15 digits.")

        return value

    # def validate_phone_number(self, value):
    #     if not re.match(r'^\d{10,15}$', value):
    #         raise serializers.ValidationError('Номер телефона должен содержать от 10 до 15 цифр.')
    #     return value
