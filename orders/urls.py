from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderRegisterViewSet, OrderViewSet, OrderItemsViewSet

router = DefaultRouter()
router.register(r'order-registers', OrderRegisterViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
