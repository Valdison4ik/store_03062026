from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from store.models import Product
from store.serializers import ProductSerializer, ProductCreateUpdateSerializer


class ProductListCreateViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # authentication_classes = [BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCreateUpdateSerializer
        return self.serializer_class


class ProductUpdateDestroyViewSet(mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.serializer_class
        return ProductCreateUpdateSerializer

