from rest_framework import viewsets
from rest_framework import filters
from .models import Quotation, QuoteItem, Sale, SaleItem, Invoice, InvoiceItem, CustomerPayment, CreditNote, CrnoteItem
from .serializers import QuotationSerializer, QuoteItemSerializer, SaleSerializer, SaleItemSerializer, InvoiceSerializer, InvoiceItemSerializer, CustomerPaymentSerializer, CreditNoteSerializer, CrnoteItemSerializer,PaymentSerializer,CheckoutSerializer
from .scripts import Checkout
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
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CheckoutView(APIView):
    def post(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            sales_id = serializer.validated_data['sales_id']
            payment_type = serializer.validated_data['payment_type']
            payments_data = serializer.validated_data.get('payments', [])
            
            payments = {payment['payment_method_id']: payment['amount'] for payment in payments_data}
            
            success = Checkout(sales_id, payments, payment_type)
            if success:
                return Response({"message": "Checkout completed successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Checkout failed."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
