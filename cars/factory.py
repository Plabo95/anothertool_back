import random
from clients.factory import ClientFactory
from .models import Car
from clients.models import Client

import factory
from faker_vehicle import VehicleProvider
from factory.django import DjangoModelFactory
from factory import SubFactory


factory.Faker.add_provider(VehicleProvider)


class CarFactory(DjangoModelFactory):

    plate = factory.Faker("license_plate")
    brand = factory.Faker("vehicle_make")
    model = factory.Faker("vehicle_model")

    client = SubFactory(ClientFactory)

    class Meta:
        model = Car
