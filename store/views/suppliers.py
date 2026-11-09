from rest_framework import viewsets

from store.models import Supplier
from store.serializers import SupplierSerializer


class SupplierUpdateViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer