import random
from clients.factory import ClientFactory
from cars.factory import CarFactory
from orders.choices import OrderState
from .models import Order
from cars.models import Car

import factory
from factory import SubFactory, fuzzy
from factory.django import DjangoModelFactory


class OrderFactory(DjangoModelFactory):
    date_in = factory.Faker("date_time_this_month")
    date_out = factory.Faker("date_time_this_month")
    client_desc = factory.Faker("text")
    diagnostic = factory.Faker("text")
    status = factory.fuzzy.FuzzyChoice(OrderState.values)

    car = SubFactory(CarFactory)

    class Meta:
        model = Order
