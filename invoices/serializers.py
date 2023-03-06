from invoices.models import Invoice, InvoiceItem
from clients.models import *
from clients.serializers import ClientSerializer
from rest_framework import serializers


class InvoiceSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        exclude = ['user',]


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        exclude = ['user',]
