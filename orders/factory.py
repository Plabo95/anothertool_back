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
    created_at = factory.Faker("date_time")
    date_in = factory.Faker("date_time")
    date_out = factory.Faker("date_time")
    client_desc = factory.Faker("text")
    diagnostic = factory.Faker("text")
    status = fuzzy.FuzzyChoice(OrderState.values).fuzz()

    car = SubFactory(CarFactory)

    class Meta:
        model = Order
