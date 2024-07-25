from rest_framework import viewsets, filters
from .models import OrderRegister, Order, OrderItems
from .serializers import OrderRegisterSerializer, OrderSerializer, OrderItemsSerializer

class OrderRegisterViewSet(viewsets.ModelViewSet):
    queryset = OrderRegister.objects.all()
    serializer_class = OrderRegisterSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['branch_of__name', 'status']
    ordering_fields = ['started', 'ended', 'status']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['customer__name', 'table__name', 'order_type', 'status']
    ordering_fields = ['created', 'total_amount', 'expected_delivery_time']

class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['order__id', 'food_item__name', 'status']
    ordering_fields = ['timestamp', 'price', 'total']
