from invoices.models import Invoice, InvoiceItem
from clients.models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ('concept', 'description', 'price',
                  'quantity', 'price', 'tax')


class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['invoice_number', 'date', 'expiring_date',
                  'status', 'client', 'taxes', 'total', 'items']

    # Method to create first the parent and then all the child objects associated
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)
        for invoice_item in items_data:
            InvoiceItem.objects.create(invoice=invoice, **invoice_item)
        return invoice
