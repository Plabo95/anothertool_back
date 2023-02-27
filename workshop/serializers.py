from workshop.models import *
from rest_framework import serializers


class WorkshopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workshop
        exclude = ['created_at', 'updated_at']
