from clients.models import *
from cars.serializers import CarSerializer
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        exclude = ['user', 'moroso']
