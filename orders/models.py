from django.db import models
from commons.models import TimeStampModel

from .choices import OrderState
from cars.models import Car


# refering to Work Orders
class Order(TimeStampModel):
    date_in = models.DateTimeField(blank=True, null=True)
    date_out = models.DateTimeField(blank=True, null=True)
    client_desc = models.TextField(blank=True, null=True)
    diagnostic = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=100, choices=OrderState.choices, default=OrderState.PENDING)

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
