# Generated by Django 3.0 on 2022-05-24 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_maintenance_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='owner',
        ),
    ]
