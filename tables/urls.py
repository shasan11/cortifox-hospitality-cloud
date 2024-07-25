from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FloorViewSet, TableViewSet, TableReservationViewSet

router = DefaultRouter()
router.register(r'floors', FloorViewSet)
router.register(r'tables', TableViewSet)
router.register(r'table-reservations', TableReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
