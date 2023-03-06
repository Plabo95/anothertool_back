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

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)


class Invoice(TimeStampModel):
    invoice_number = models.IntegerField(db_index=True)
    date = models.DateTimeField()
    status = models.CharField(max_length=100, choices=InvoiceStatus.choices,
                              default=InvoiceStatus.PENDING)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(
        InvoiceItem, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
