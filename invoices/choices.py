from django.db import models


class InvoiceStatus(models.TextChoices):
    PENDING = 'Pendiente'
    EXPIRED = 'Caducada'
    PAYED = 'Pagada'


class InvoiceItemTax(models.TextChoices):
    TEN = 'ten', 'IVA 10%'
    TWENTY = 'twenty', "IVA 21%"
    EXENT = "exento", 'Exento'
    NO = "no", 'No sujeto'
