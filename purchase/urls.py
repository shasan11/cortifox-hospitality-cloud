from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PurchaseOrderViewSet, PurchaseOrderItemViewSet, PurchaseBillsViewSet, PurchaseBillsItemsViewSet, SupplierPaymentViewSet,DebitNoteViewSet

router = DefaultRouter()
router.register(r'purchase-orders', PurchaseOrderViewSet)
router.register(r'purchase-order-items', PurchaseOrderItemViewSet)
router.register(r'purchase-bills', PurchaseBillsViewSet)
router.register(r'purchase-bills-items', PurchaseBillsItemsViewSet)
router.register(r'supplier-payments', SupplierPaymentViewSet)
router.register(r'debit-notes', DebitNoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
