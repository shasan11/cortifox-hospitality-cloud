from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Unit, VariantAttribute, VariantAttributeItem, Product
from .serializers import CategorySerializer, UnitSerializer, VariantAttributeSerializer, VariantAttributeItemSerializer, ProductSerializer
from .filters import CategoryFilter, UnitFilter, VariantAttributeFilter, VariantAttributeItemFilter, ProductFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = CategoryFilter
    search_fields = ['name', 'desc']
    ordering_fields = ['name', 'created_at']

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = UnitFilter
    search_fields = ['name', 'desc']
    ordering_fields = ['name', 'created_at']

class VariantAttributeViewSet(viewsets.ModelViewSet):
    queryset = VariantAttribute.objects.all()
    serializer_class = VariantAttributeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = VariantAttributeFilter
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']

class VariantAttributeItemViewSet(viewsets.ModelViewSet):
    queryset = VariantAttributeItem.objects.all()
    serializer_class = VariantAttributeItemSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = VariantAttributeItemFilter
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'code', 'desc']
    ordering_fields = ['name', 'created_at', 'selling_price']
