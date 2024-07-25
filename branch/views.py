from rest_framework import viewsets, filters
from .models import Branch
from .serializers import BranchSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'pan', 'crid', 'pro', 'province', 'district', 'city', 'street_add', 'email', 'phone']
    ordering_fields = ['name', 'province', 'district', 'city', 'balance', 'created_at', 'updated_at']
