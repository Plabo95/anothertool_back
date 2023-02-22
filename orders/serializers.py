from rest_framework import serializers
from .models import Order
from cars.serializers import CarSerializer


class OrderSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'date_in', 'date_out', 'client_desc',
                  'diagnostic', 'status', 'car', 'created_at')
        # exclude = ['user']


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'date_in', 'date_out', 'client_desc',
                  'diagnostic', 'status', 'car')


class OrderStatsSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True, format="%d-%m-%Y")
    created_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ('date', 'created_count',)
        # exclude = ['user']
