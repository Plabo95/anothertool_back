from rest_framework import permissions
from rest_framework import viewsets

from .models import *
from .serializers import *


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return CreateOrderSerializer
        else:
            return OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
