from django.db import models
from django.contrib.auth import get_user_model
from clients.models import Client

from commons.models import TimeStampModel


class Car(TimeStampModel):
    plate = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return (self.brand + '' + self.model)
