from django.db import models
from commons.models import TimeStampModel


# refering to Work Orders
class Workshop(TimeStampModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(blank=True, null=True, max_length=16, unique=True)
    email = models.EmailField(unique=True)