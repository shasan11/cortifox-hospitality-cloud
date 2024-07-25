from rest_framework import viewsets, filters
from .models import ChartofAccounts, BankAccounts, Currency, PaymentMethod, JournalEntry, JournalEntryItems, CashTransfers, ChequeRegister
from .serializers import ChartofAccountsSerializer, BankAccountsSerializer, CurrencySerializer, PaymentMethodSerializer, JournalEntrySerializer, JournalEntryItemsSerializer, CashTransfersSerializer, ChequeRegisterSerializer

class ChartofAccountsViewSet(viewsets.ModelViewSet):
    queryset = ChartofAccounts.objects.all()
    serializer_class = ChartofAccountsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'coa_type']
    ordering_fields = ['created', 'updated', 'name']

class BankAccountsViewSet(viewsets.ModelViewSet):
    queryset = BankAccounts.objects.all()
    serializer_class = BankAccountsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code', 'acc_type']
    ordering_fields = ['created', 'updated', 'name']

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'symbol']
    ordering_fields = ['created', 'updated', 'name']

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created', 'updated', 'name']

class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['bill_no', 'notes']
    ordering_fields = ['created', 'updated', 'date']

class JournalEntryItemsViewSet(viewsets.ModelViewSet):
    queryset = JournalEntryItems.objects.all()
    serializer_class = JournalEntryItemsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['journal_entry__bill_no', 'chart_of_accounts__name']
    ordering_fields = ['created', 'updated', 'dr_amount', 'cr_amount']

class CashTransfersViewSet(viewsets.ModelViewSet):
    queryset = CashTransfers.objects.all()
    serializer_class = CashTransfersSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['bill_no', 'notes']
    ordering_fields = ['created', 'updated', 'date']

class ChequeRegisterViewSet(viewsets.ModelViewSet):
    queryset = ChequeRegister.objects.all()
    serializer_class = ChequeRegisterSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['reference', 'cheque_no', 'payee_name']
    ordering_fields = ['created', 'updated', 'issued_date']
