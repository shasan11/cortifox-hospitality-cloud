from rest_framework import serializers
from .models import Quotation, QuoteItem, Sale, SaleItem, Invoice, InvoiceItem, CustomerPayment, CreditNote, CrnoteItem

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = '__all__'

class QuoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteItem
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'

class CustomerPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPayment
        fields = '__all__'

class CreditNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditNote
        fields = '__all__'

class CrnoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrnoteItem
        fields = '__all__'
