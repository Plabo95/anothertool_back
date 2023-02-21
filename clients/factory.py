
from .models import Client
from factory.django import DjangoModelFactory
import faker

faker = faker.Faker(locale="es_ES")


class ClientFactory(DjangoModelFactory):
    name = faker.name()
    phone = faker.phone_number()
    email = faker.email()

    class Meta:
        model = Client
