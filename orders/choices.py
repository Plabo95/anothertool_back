from django.db import models


class OrderStatus(models.TextChoices):
    PENDING = "pending"
    STARTED = "started"
    COMPLETED = "completed"
