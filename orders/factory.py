
from clients.factory import ClientFactory
from cars.factory import CarFactory
from orders.choices import OrderState
from .models import Order

import factory
from factory import SubFactory, fuzzy
from factory.django import DjangoModelFactory
from factory.faker import faker
import faker

faker = faker.Faker(locale="es_ES")


class OrderFactory(DjangoModelFactory):
    date_in: faker.date_time()
    date_out: faker.date_time()
    client_desc: faker.text()
    diagnostic: faker.text()
    status: fuzzy.FuzzyChoice(OrderState.values).fuzz()

    car = SubFactory(CarFactory)

    class Meta:
        model = Order
