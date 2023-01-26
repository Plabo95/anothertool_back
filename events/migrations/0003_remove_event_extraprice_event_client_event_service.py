# Generated by Django 4.1.5 on 2023-01-26 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('services', '0001_initial'),
        ('events', '0002_remove_event_client_remove_event_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='extraprice',
        ),
        migrations.AddField(
            model_name='event',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
        migrations.AddField(
            model_name='event',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
    ]
