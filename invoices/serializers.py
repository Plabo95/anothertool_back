from invoices.models import Invoice, InvoiceItem
from clients.models import *
from clients.serializers import ClientSerializer
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ('concept', 'price', 'quantity', 'price', 'tax',)


class InvoiceSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    item = InvoiceItemSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ('invoice_number', 'date', 'expiring_date',
                  'status', 'client', 'item',)
