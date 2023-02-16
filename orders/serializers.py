from rest_framework import serializers
from .models import Order
from .choices import OrderState


class OrderSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(
        source='client.name', read_only=True)

    class Meta:
        model = Order
        fields = ('__all__')
        # exclude = ['user']
