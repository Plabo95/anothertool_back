from django.db import models
from services.models import *

from django.contrib.auth import get_user_model
from clients.models import *

# Create your models here.
class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null = True) 
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True) 
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    paid = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    user= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
