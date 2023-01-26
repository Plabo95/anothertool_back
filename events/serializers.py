from events.models import *
from services.serializers import ServiceSerializer
from clients.serializers import ClientSerializer 
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Event
        fields = '__all__'


