from django.db import models
from django.contrib.auth import get_user_model

from clients.models import Client
from commons.models import TimeStampModel
from .choices import InvoiceStatus, InvoiceItemTax


class InvoiceItem(TimeStampModel):
    concept = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.DecimalField(decimal_places=2, max_digits=10)
    tax = models.CharField(max_length=100, choices=InvoiceItemTax.choices)


class Invoice(TimeStampModel):
    invoice_number = models.IntegerField(db_index=True)
    date = models.DateTimeField()
    expiring_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=100, choices=InvoiceStatus.choices, default=InvoiceStatus.PENDING, blank=True, null=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(
        InvoiceItem)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
