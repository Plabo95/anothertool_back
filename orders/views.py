import datetime
from django.db.models import Count
from rest_framework import permissions
from rest_framework import viewsets

from django.utils import timezone
from django.db.models.functions import TruncDay
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
        period_filter = self.request.query_params.get('period')

        if period_filter:
            if period_filter == 'week':
                queryset = Order.objects.filter(date_in__lte=timezone.now(
                ), date_in__gt=timezone.now()-timezone.timedelta(days=7))
            if period_filter == 'month':
                queryset = Order.objects.filter(date_in__lte=timezone.now(
                ), date_in__gt=timezone.now()-timezone.timedelta(days=30))
            if period_filter == 'day':
                queryset = Order.objects.filter(date_in__lte=timezone.now(),
                                                date_in__gt=timezone.now()-datetime.timedelta(days=1))
        if status_filter:
            # filter by order status
            queryset = Order.objects.filter(
                status=status_filter).order_by('-created_at')
        if latest_filter:
            # Get only n latest items
            queryset = Order.objects.all().order_by(
                '-created_at')[:int(latest_filter)]

        if not status_filter and not latest_filter and not period_filter:
            queryset = Order.objects.all().order_by('-created_at')

        return queryset


class OrderStatsViewSet(viewsets.ReadOnlyModelViewSet):
    # annotate añade una anotacion en cada objeto del queryset
    # trunc by day elimina la hora
    # con values me quedo solo con el valor de fecha
    # luego vuelvo a anotar la cuenta de id's diferentes
    queryset = Order.objects.filter(date_in__lte=datetime.datetime.today(
    ), date_in__gt=datetime.datetime.today()-datetime.timedelta(days=30)).annotate(
        date=TruncDay('date_in')).values("date").annotate(created_count=Count('id'))

    serializer_class = OrderStatsSerializer
