from django.db import models
from commons.models import TimeStampModel

from .choices import OrderState
from clients.models import Client

# refering to Work Orders


class Order(TimeStampModel):
    date_in = models.DateTimeField()
    date_out = models.DateTimeField(blank=True, null=True)
    client_desc = models.TextField(blank=True, null=True)
    diagnostic = models.TextField(blank=True, null=True)
    state = models.CharField(
        max_length=100, choices=OrderState.choices, default=OrderState.PENDING)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
