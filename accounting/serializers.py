from rest_framework import serializers
from .models import ChartofAccounts, BankAccounts, Currency, PaymentMethod, JournalEntry, JournalEntryItems, CashTransfers, ChequeRegister

class ChartofAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartofAccounts
        fields = '__all__'

class BankAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccounts
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = '__all__'

class JournalEntryItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntryItems
        fields = '__all__'

class CashTransfersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashTransfers
        fields = '__all__'

class ChequeRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChequeRegister
        fields = '__all__'
