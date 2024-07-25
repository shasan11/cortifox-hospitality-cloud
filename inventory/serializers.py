from rest_framework import serializers
from .models import Category, Unit, VariantAttribute, VariantAttributeItem, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class VariantAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantAttribute
        fields = '__all__'

class VariantAttributeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantAttributeItem
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
