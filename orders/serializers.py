from rest_framework import serializers
from .models import OrderRegister, Order, OrderItems

class OrderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRegister
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'
