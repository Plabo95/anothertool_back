from invoices.models import Invoice, InvoiceItem
from clients.models import *
from clients.serializers import ClientSerializer
from rest_framework import serializers


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        exclude = ['user',]


class InvoiceSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=True, read_only=True)
    item = InvoiceItemSerializer(many=True)

    class Meta:
        model = Invoice
        exclude = ['user',]
