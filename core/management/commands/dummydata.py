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
        print('Deleting all db registers...')
        Client.objects.all().delete()
        Car.objects.all().delete()
        Order.objects.all().delete()

        print('Generating new data...')
        # ClientFactory.create_batch(20)
        # CarFactory.create_batch(15)
        OrderFactory.create_batch(10)
