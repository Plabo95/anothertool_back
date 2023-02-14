from .models import *

from rest_framework import serializers


class RepairOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairOrder
        #exclude = ['user']