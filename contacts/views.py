from rest_framework import viewsets, filters
from .models import ContactGroup, Contact
from .serializers import ContactGroupSerializer, ContactSerializer

class ContactGroupViewSet(viewsets.ModelViewSet):
    queryset = ContactGroup.objects.all()
    serializer_class = ContactGroupSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'type']
    ordering_fields = ['name', 'type', 'created_at']


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'contact_type', 'phone', 'email']
    ordering_fields = ['name', 'contact_type', 'created_at']
