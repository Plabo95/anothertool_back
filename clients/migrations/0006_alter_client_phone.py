# Generated by Django 4.1.5 on 2023-02-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_rename_telf_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
