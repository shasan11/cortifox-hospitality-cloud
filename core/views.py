from rest_framework import viewsets, filters
from .models import CustomUser, UserBatch, AppUsers
from .serializers import CustomUserSerializer, UserBatchSerializer, AppUsersSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name', 'branch__name']
    ordering_fields = ['username', 'email', 'first_name', 'last_name', 'branch']

class UserBatchViewSet(viewsets.ModelViewSet):
    queryset = UserBatch.objects.all()
    serializer_class = UserBatchSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['branch__name', 'created_at']
    ordering_fields = ['created_at']

class AppUsersViewSet(viewsets.ModelViewSet):
    queryset = AppUsers.objects.all()
    serializer_class = AppUsersSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['fname', 'lname', 'email', 'username', 'branch_of__name', 'group_assigned__name']
    ordering_fields = ['fname', 'lname', 'email', 'username', 'branch_of', 'group_assigned']
