# Generated by Django 4.1.5 on 2023-02-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
