from django.db import models
from django.contrib.auth import get_user_model

from clients.models import Client
from commons.models import TimeStampModel


class InvoiceItem(TimeStampModel):
    concept = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.DecimalField(decimal_places=2, max_digits=10)
    iva = models.DecimalField(decimal_places=2, max_digits=10)


class Invoice(TimeStampModel):
    invoice_number = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(
        InvoiceItem, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
