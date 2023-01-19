from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    telf = models.CharField(blank=True, null=True, max_length=16)
    moroso = models.BooleanField(default=False)
    user= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name