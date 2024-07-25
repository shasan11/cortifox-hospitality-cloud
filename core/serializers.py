from rest_framework import serializers
from .models import CustomUser, UserBatch, AppUsers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBatch
        fields = '__all__'

class AppUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsers
        fields = '__all__'
