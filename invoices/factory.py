from core.models import User
from clients.models import Client
from invoices.choices import InvoiceItemTax, InvoiceStatus
from invoices.models import Invoice, InvoiceItem

import random
import factory
import factory.fuzzy


class InvoiceFactory(factory.django.DjangoModelFactory):
    invoice_number = factory.Faker("pyint", min_value=0,
                                   max_value=100000,)
    date = factory.Faker("date_time_this_month")
    expiring_date = factory.Faker("date_time_this_month")
    status = factory.fuzzy.FuzzyChoice(choices=InvoiceStatus.choices).fuzz()
    taxes = factory.Faker("pyfloat", min_value=0,
                          max_value=10000, right_digits=2)
    total = factory.Faker("pyfloat", min_value=0,
                          max_value=10000, right_digits=2)

    client = random.choice(Client.objects.all())
    user = User.objects.get(id=2)

    class Meta:
        model = Invoice


class InvoiceItemFactory(factory.django.DjangoModelFactory):
    concept = factory.Faker("text")
    description = factory.Faker("text")
    price = factory.Faker("random_int", min=0, max=1000)
    quantity = factory.Faker("random_int", min=0, max=100)
    tax = factory.fuzzy.FuzzyChoice(InvoiceItemTax.choices).fuzz()

    invoice = random.choice(Invoice.objects.all())

    class Meta:
        model = InvoiceItem
