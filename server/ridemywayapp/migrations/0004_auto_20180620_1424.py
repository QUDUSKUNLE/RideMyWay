# Generated by Django 2.0.6 on 2018-06-20 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ridemywayapp', '0003_auto_20180620_1416'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Rider',
        ),
    ]
