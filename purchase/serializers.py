from rest_framework import serializers
from .models import PurchaseOrder, PurchaseOrderItem, PurchaseBills, PurchaseBillsItems, SupplierPayment, DebitNote

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'

class PurchaseBillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseBills
        fields = '__all__'

class PurchaseBillsItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseBillsItems
        fields = '__all__'

class SupplierPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierPayment
        fields = '__all__'

class DebitNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitNote
        fields = '__all__'
