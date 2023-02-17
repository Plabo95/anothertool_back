# Generated by Django 4.1.5 on 2023-02-17 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_rename_telf_client_phone'),
        ('cars', '0005_alter_car_brand_alter_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='clients.client'),
        ),
    ]
