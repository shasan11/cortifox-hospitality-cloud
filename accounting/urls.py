from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChartofAccountsViewSet, BankAccountsViewSet, CurrencyViewSet, PaymentMethodViewSet, JournalEntryViewSet, JournalEntryItemsViewSet, CashTransfersViewSet, ChequeRegisterViewSet

router = DefaultRouter()
router.register(r'chart-of-accounts', ChartofAccountsViewSet)
router.register(r'bank-accounts', BankAccountsViewSet)
router.register(r'currency', CurrencyViewSet)
router.register(r'payment-methods', PaymentMethodViewSet)
router.register(r'journal-entries', JournalEntryViewSet)
router.register(r'journal-entry-items', JournalEntryItemsViewSet)
router.register(r'cash-transfers', CashTransfersViewSet)
router.register(r'cheque-register', ChequeRegisterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
