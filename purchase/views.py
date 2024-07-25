from rest_framework import viewsets
from rest_framework import filters
from .models import PurchaseOrder, PurchaseOrderItem, PurchaseBills, PurchaseBillsItems, SupplierPayment,DebitNote
from .serializers import PurchaseOrderSerializer, PurchaseOrderItemSerializer, PurchaseBillsSerializer, PurchaseBillsItemsSerializer, SupplierPaymentSerializer, DebitNoteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import OrderingFilter
class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    filter_backends = [filters.OrderingFilter,  DjangoFilterBackend]
    ordering_fields = '__all__'
    ordering = ['date']

class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer
    filter_backends = [filters.OrderingFilter,  DjangoFilterBackend]
    ordering_fields = '__all__'
    ordering = ['quotation']

class PurchaseBillsViewSet(viewsets.ModelViewSet):
    queryset = PurchaseBills.objects.all()
    serializer_class = PurchaseBillsSerializer
    filter_backends = [filters.OrderingFilter,  DjangoFilterBackend]
    ordering_fields = '__all__'
    ordering = ['date']

class PurchaseBillsItemsViewSet(viewsets.ModelViewSet):
    queryset = PurchaseBillsItems.objects.all()
    serializer_class = PurchaseBillsItemsSerializer
    filter_backends = [filters.OrderingFilter,  DjangoFilterBackend]
    ordering_fields = '__all__'
    ordering = ['sale']

class SupplierPaymentViewSet(viewsets.ModelViewSet):
    queryset = SupplierPayment.objects.all()
    serializer_class = SupplierPaymentSerializer
    filter_backends = [filters.OrderingFilter,  DjangoFilterBackend]
    ordering_fields = '__all__'
    ordering = ['date']
class DebitNoteViewSet(viewsets.ModelViewSet):
    queryset = DebitNote.objects.all()
    serializer_class = DebitNoteSerializer
    filter_backends = [filters.OrderingFilter,  DjangoFilterBackend]
    ordering_fields = '__all__'
    ordering = ['date']
