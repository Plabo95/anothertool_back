# Generated by Django 4.1.5 on 2023-02-17 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='state',
            new_name='status',
        ),
    ]
