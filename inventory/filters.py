from django_filters import rest_framework as filters
from .models import Category, Unit, VariantAttribute, VariantAttributeItem, Product

class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'name': ['exact', 'icontains'],
            'active': ['exact'],
            'created_at': ['gte', 'lte'],
        }

class UnitFilter(filters.FilterSet):
    class Meta:
        model = Unit
        fields = {
            'name': ['exact', 'icontains'],
            'active': ['exact'],
            'created_at': ['gte', 'lte'],
        }

class VariantAttributeFilter(filters.FilterSet):
    class Meta:
        model = VariantAttribute
        fields = {
            'name': ['exact', 'icontains'],
            'active': ['exact'],
            'created_at': ['gte', 'lte'],
        }

class VariantAttributeItemFilter(filters.FilterSet):
    class Meta:
        model = VariantAttributeItem
        fields = {
            'name': ['exact', 'icontains'],
            'variant_attribute': ['exact'],
            'active': ['exact'],
            'created_at': ['gte', 'lte'],
        }

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['exact', 'icontains'],
            'category': ['exact'],
            'tax_type': ['exact'],
            'type': ['exact'],
            'active': ['exact'],
            'created_at': ['gte', 'lte'],
        }
