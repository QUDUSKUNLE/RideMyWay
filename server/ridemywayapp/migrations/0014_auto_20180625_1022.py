# Generated by Django 2.0.6 on 2018-06-25 10:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ridemywayapp', '0013_auto_20180625_1017'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rides',
            new_name='OfferRides',
        ),
    ]