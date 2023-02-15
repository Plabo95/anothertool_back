from django.db import models
from django.contrib.auth import get_user_model

from commons.models import TimeStampModel


class Client(TimeStampModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(blank=True, null=True, unique=True, max_length=16)
    email = models.EmailField(unique=True)
    moroso = models.BooleanField(default=False)

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
