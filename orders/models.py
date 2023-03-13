from django.contrib.auth import get_user_model

from django.db import models
from commons.models import TimeStampModel

from orders.choices import OrderStatus
from cars.models import Car
from invoices.models import Invoice

# refering to Work Orders


class Order(TimeStampModel):
    date_in = models.DateTimeField(blank=True, null=True)
    date_out = models.DateTimeField(blank=True, null=True)
    client_desc = models.TextField(blank=True, null=True)
    diagnostic = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=100, choices=OrderStatus.choices, default=OrderStatus.PENDING)

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)

    def has_invoice(self):
        try:
            Invoice.objects.get(order=self.id)
            return True
        except:
            return False
