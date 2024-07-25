from rest_framework import serializers
from .models import ContactGroup, Contact

class ContactGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactGroup
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
