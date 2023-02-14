from django.db import models
from commons.models import TimeStampModel

from .choices import RepairOrderState
from cars.models import Car

class RepairOrder(TimeStampModel):
    date_in = models.DateTimeField()
    date_out = models.DateTimeField(blank=True, null=True)
    client_desc = models.TextField(blank=True, null=True)
    diagnostic = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=100, choices = RepairOrderState.choices, default=RepairOrderState.PENDING)
    
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
