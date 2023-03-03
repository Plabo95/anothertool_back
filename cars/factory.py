from clients.factory import ClientFactory
from .models import Car
from core.models import User

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
    user = User.objects.get(id=2)

    class Meta:
        model = Car
