from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CategoryViewSet, UnitViewSet, VariantAttributeViewSet,
                    VariantAttributeItemViewSet, ProductViewSet)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'units', UnitViewSet)
router.register(r'variant-attributes', VariantAttributeViewSet)
router.register(r'variant-attribute-items', VariantAttributeItemViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
