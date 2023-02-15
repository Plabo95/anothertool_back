from django.db import models
from django.contrib.auth import get_user_model
from clients.models import Client

from commons.models import TimeStampModel


class Car(TimeStampModel):
    plate = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return (self.brand + '' + self.model)
