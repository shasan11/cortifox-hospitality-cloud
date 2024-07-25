from rest_framework import serializers
from .models import Floor, Table, TableReservation

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class TableReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableReservation
        fields = '__all__'
