from django.db import models


class OrderState(models.TextChoices):
    PENDING = "pending"
    STARTED = "started"
    COMPLETED = "completed"
