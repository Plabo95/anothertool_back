from clients.factory import ClientFactory
from .models import Car
from clients.models import Client

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import faker
import faker

faker = faker.Faker(locale="es_ES")


class CarFactory(DjangoModelFactory):
    plate: faker.name()
    brand: faker.company()
    model: faker.company()

    client = Client.objects.all()[0]
    # SubFactory(ClientFactory)

    class Meta:
        model = Car
