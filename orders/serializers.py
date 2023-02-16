from rest_framework import serializers
from .models import Order
from .choices import OrderState


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')
        # exclude = ['user']
