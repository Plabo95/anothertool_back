from django.db import models

from django.contrib.auth import get_user_model
from clients.models import *

# Create your models here.
class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null = True) 
    extraprice = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default="Default")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    paid = models.BooleanField(default=False)
    user= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    @property
    def client_name(self):
        try:
            cn=self.client.name
        except:
            cn='Sin nombre'
        return(cn)
    
    @property
    def client_car(self):
        try:
            cc=self.client.car.brand
        except:
            cc='Sin coche'
        return(cc)

    @property
    def service_name(self):
        try:
            sn=self.service.name
        except:
            sn='Sin nombre'
        return(sn)
    
    @property
    def service_color(self):
        try:
            sc=self.service.color
        except:
            sc='grey'
        return(sc)

    def save(self, *args, **kwargs):        #Defino el metodo save para cada cita que se guarde, si no la ha pagado le pongo en morosos
        super().save(*args, **kwargs)
        sinpa = Event.objects.filter(client=self.client.id, paid=False).count()      #Busco si tiene mas citas sin pagar
        if self.paid == True and sinpa<1: 
            Client.objects.filter(pk=self.client.id).update(moroso=False)
        else:                
            Client.objects.filter(pk=self.client.id).update(moroso=True)