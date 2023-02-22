
from .models import Client
from factory.django import DjangoModelFactory
import factory
# import faker

# faker = faker.Faker(locale="es_ES")


class ClientFactory(DjangoModelFactory):
    name = factory.Faker("name")
    phone = factory.Faker("phone_number")
    email = factory.Faker("email")

    class Meta:
        model = Client
