from clients.factory import ClientFactory
from .models import Car
from clients.models import Client

from faker_vehicle import VehicleProvider
from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import faker
import faker

faker = faker.Faker(locale="es_ES")
faker.add_provider(VehicleProvider)


class CarFactory(DjangoModelFactory):
    class Meta:
        model = Car

    plate = faker.license_plate()
    brand = faker.vehicle_make()
    model = faker.vehicle_model()

    client = SubFactory(ClientFactory)
