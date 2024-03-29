from core.models import User
from cars.factory import CarFactory
from invoices.choices import OrderStatus
from .models import Order

import factory
from factory import SubFactory


class OrderFactory(factory.django.DjangoModelFactory):
    date_in = factory.Faker("date_time_this_month")
    date_out = factory.Faker("date_time_this_month")
    client_desc = factory.Faker("text")
    diagnostic = factory.Faker("text")
    status = factory.fuzzy.FuzzyChoice(OrderStatus.values)

    car = SubFactory(CarFactory)
    user = User.objects.get(id=2)

    class Meta:
        model = Order
