from django.db import models
from django.contrib.auth import get_user_model

from colorfield.fields import ColorField


class Service(models.Model):
    name = models.CharField(max_length=100)
    estimed_hours = models.IntegerField(blank=True, null=True)            #Time in hours
    estimed_mins = models.IntegerField(blank=True, null=True)            #Time in mins
    baseprice = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    color = ColorField(default='#FF0000')
    user= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name