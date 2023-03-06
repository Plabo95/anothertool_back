from .models import *
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(
        source='client.name', read_only=True)

    class Meta:
        model = Car
        fields = ('id', 'client_name',
                  'plate', 'brand', 'model', 'client')
