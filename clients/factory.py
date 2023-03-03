
from .models import Client
from core.models import User
from factory.django import DjangoModelFactory
import factory
# import faker

# faker = faker.Faker(locale="es_ES")


class ClientFactory(DjangoModelFactory):
    name = factory.Faker("name")
    phone = factory.Faker("phone_number")
    email = factory.Faker("email")

    user = User.objects.get(id=2)

    class Meta:
        model = Client
