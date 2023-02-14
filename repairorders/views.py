from .models import *
from .serializers import *

#RF
from rest_framework import permissions
from rest_framework import viewsets

class RepairOrderViewset(viewsets.ModelViewSet):
    queryset = RepairOrder.objects.all()
    serializer_class = RepairOrderSerializer
    #permission_classes = [permissions.IsAuthenticated]

    #def perform_create(self, serializer):
        #serializer.save(user=self.request.user)