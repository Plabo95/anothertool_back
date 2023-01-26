from services.serializers import ServiceSerializer
from services.models import *

from rest_framework import viewsets

class ServiceViewSet(viewsets.ModelViewSet):
    #list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy()
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    #permission_classes = [permissions.IsAuthenticated]

