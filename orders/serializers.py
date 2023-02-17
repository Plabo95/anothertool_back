from rest_framework import serializers
from .models import Order
from cars.serializers import CarSerializer


class OrderSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'date_in', 'date_out', 'client_desc',
                  'diagnostic', 'status', 'car')
        # exclude = ['user']


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'date_in', 'date_out', 'client_desc',
                  'diagnostic', 'status', 'car')
