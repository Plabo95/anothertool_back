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
    orders_count = serializers.SerializerMethodField()
    pending_orders_count = serializers.SerializerMethodField()
    started_orders_count = serializers.SerializerMethodField()
    completed_orders_count = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('orders_count', 'pending_orders_count',
                  'started_orders_count', 'completed_orders_count')
        # exclude = ['user']

    def get_orders_count(self, obj):
        return Order.objects.count()

    def get_pending_orders_count(self, obj):
        return Order.objects.filter(status='pending').count()

    def get_started_orders_count(self, obj):
        return Order.objects.filter(status='started').count()

    def get_completed_orders_count(self, obj):
        return Order.objects.filter(status='completed').count()
