from workshop.models import *
from workshop.serializers import *

# RF
from rest_framework import permissions
from rest_framework import viewsets


class WorkshopViewset(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
