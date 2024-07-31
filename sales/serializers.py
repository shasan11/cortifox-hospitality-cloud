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
from rest_framework import serializers

class PaymentSerializer(serializers.Serializer):
    payment_method_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

class CheckoutSerializer(serializers.Serializer):
    sales_id = serializers.IntegerField()
    payment_type = serializers.ChoiceField(choices=["Complementary", "Pay Later", "Split Payment"])
    payments = serializers.ListSerializer(child=PaymentSerializer(), required=False)
