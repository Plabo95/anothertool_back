import datetime
from django.db.models import Count
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
        status_filter = self.request.query_params.get('status')
        latest_filter = self.request.query_params.get('latest')

        if status_filter:
            # filter by order status
            queryset = Order.objects.filter(
                status=status_filter).order_by('-created_at')
        elif latest_filter:
            # Get only n latest items
            queryset = Order.objects.all().order_by(
                '-created_at')[:int(latest_filter)]
        else:
            queryset = Order.objects.all().order_by('-created_at')

        return queryset


class OrderStatsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This only has list and retrieve.
    """
    queryset = Order.objects.order_by(
        'created_at').values('created_at').distinct()
    # queryset = Order.objects.filter(created_at__lte=datetime.datetime.today(
    # ), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30)).distinct('created_at')
    serializer_class = OrderStatsSerializer
