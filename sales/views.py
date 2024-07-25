from rest_framework import viewsets
from rest_framework import filters
from .models import Quotation, QuoteItem, Sale, SaleItem, Invoice, InvoiceItem, CustomerPayment, CreditNote, CrnoteItem
from .serializers import QuotationSerializer, QuoteItemSerializer, SaleSerializer, SaleItemSerializer, InvoiceSerializer, InvoiceItemSerializer, CustomerPaymentSerializer, CreditNoteSerializer, CrnoteItemSerializer

class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['date']

class QuoteItemViewSet(viewsets.ModelViewSet):
    queryset = QuoteItem.objects.all()
    serializer_class = QuoteItemSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['quotation']

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['date']

class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['sale']

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['date']

class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['invoice']

class CustomerPaymentViewSet(viewsets.ModelViewSet):
    queryset = CustomerPayment.objects.all()
    serializer_class = CustomerPaymentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['date']

class CreditNoteViewSet(viewsets.ModelViewSet):
    queryset = CreditNote.objects.all()
    serializer_class = CreditNoteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['date']

class CrnoteItemViewSet(viewsets.ModelViewSet):
    queryset = CrnoteItem.objects.all()
    serializer_class = CrnoteItemSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['credit_note']
