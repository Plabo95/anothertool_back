from rest_framework import permissions
from rest_framework import viewsets

from .models import *
from .serializers import *


class OrderViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return CreateOrderSerializer
        else:
            return OrderSerializer

    # Si paso un queryset en la url es para filtrar por estado
    def get_queryset(self):
        filter_by = self.request.query_params.get('status')

        if filter_by:
            queryset = Order.objects.filter(
                status=filter_by).order_by('-updated_at')
        else:
            queryset = Order.objects.all().order_by('-updated_at')

        return queryset
