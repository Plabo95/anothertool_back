from django.db import models


class RepairOrderState(models.TextChoices):
    PENDING = "pending"
    STARTED = "started"
    TESTING = "testing"
    FINISHED = "finished"