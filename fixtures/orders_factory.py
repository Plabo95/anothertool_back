import faker

faker = faker.Faker(locale="es_ES")

date_in = models.DateTimeField(blank=True, null=True)
date_out = models.DateTimeField(blank=True, null=True)
client_desc = models.TextField(blank=True, null=True)
diagnostic = models.TextField(blank=True, null=True)
status = models.CharField(
    max_length=100, choices=OrderState.choices, default=OrderState.PENDING)

car = models.ForeignKey(Car, on_delete=models.CASCADE)

fake_order = {
    date_in: faker.date_time(),
    date_out: faker.date_time(),
    client_desc: faker.text(),
    diagnostic: faker.text(),
    status: faker.
}
