# Generated by Django 2.0.6 on 2018-06-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridemywayapp', '0009_auto_20180621_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='ride_id',
            field=models.CharField(blank=True, editable=False, max_length=255, primary_key=True, serialize=False),
        ),
    ]
