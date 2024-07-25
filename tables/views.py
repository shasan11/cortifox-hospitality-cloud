from rest_framework import viewsets, filters
from .models import Floor, Table, TableReservation
from .serializers import FloorSerializer, TableSerializer, TableReservationSerializer

class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['floorname']
    ordering_fields = ['sno', 'floorname', 'created_at']


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'status', 'floor__floorname']
    ordering_fields = ['name', 'status', 'created_at']


class TableReservationViewSet(viewsets.ModelViewSet):
    queryset = TableReservation.objects.all()
    serializer_class = TableReservationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['table__name', 'customer__username']
    ordering_fields = ['reservation_start', 'reservation_end', 'created_at']
