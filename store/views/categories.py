from rest_framework import viewsets

from store.models import Category
from store.serializers import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    search_fields = ('name',)
    # ordering_fields = ('published_date', 'page_count')
    # ordering = ('-published_date',)
    # filterset_fields = {
    #     'category__slug': ['exact'],
    #     'published_date': ['year', 'year__gte', 'year__lte'],
    #     'page_count': ['gt', 'lt'],
    # }


class CategoryUpdateViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



