from django.db import transaction
from django.core.management.base import BaseCommand

from clients.factory import ClientFactory
from clients.models import Client
from orders.factory import OrderFactory
from orders.models import Order
from cars.factory import CarFactory
from cars.models import Car


class Command(BaseCommand):
    help = "Generates test data"

    def handle(self, *args, **kwargs):
        # ClientFactory.create_batch(50)
        OrderFactory.create_batch(50)
