from clients.models import *

from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['user', 'moroso']
        extra_kwargs = {
            "email": {
                "error_messages": {"unique": "Ya hay un cliente con ese email"}
            },
            "phone": {
                "error_messages": {"unique": "Ya hay un cliente con ese teléfono"}
            }
        }
