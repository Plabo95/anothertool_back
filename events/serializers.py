from events.models import *
from services.serializers import ServiceSerializer
from clients.serializers import ClientSerializer 
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    #client = ClientSerializer(many=False)
    class Meta:
        model = Event
        fields = '__all__'

    client_name = serializers.ReadOnlyField()
    service_name = serializers.ReadOnlyField()
    service_color = serializers.ReadOnlyField()

    def validate_ended(self,value):
        return value
    def validate_not_paid(self, value):
        return value

class NextEventSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=False)
    client = ClientSerializer(many=False)
    class Meta:
        model = Event
        fields = '__all__'
