from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuotationViewSet, QuoteItemViewSet, SaleViewSet, SaleItemViewSet, InvoiceViewSet, InvoiceItemViewSet, CustomerPaymentViewSet, CreditNoteViewSet, CrnoteItemViewSet

router = DefaultRouter()
router.register(r'quotations', QuotationViewSet)
router.register(r'quote-items', QuoteItemViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sale-items', SaleItemViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoice-items', InvoiceItemViewSet)
router.register(r'customer-payments', CustomerPaymentViewSet)
router.register(r'credit-notes', CreditNoteViewSet)
router.register(r'crnote-items', CrnoteItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
