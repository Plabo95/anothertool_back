from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Car(models.Model):
    plate = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)    
    model = models.CharField(max_length=100)
    user= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return (self.brand + '' + self.model)