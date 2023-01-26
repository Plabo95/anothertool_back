from clients.models import *
from clients.serializers import *

#RF
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    #permission_classes = [permissions.IsAuthenticated]
