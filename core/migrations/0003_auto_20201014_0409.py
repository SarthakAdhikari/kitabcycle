# Generated by Django 3.1.1 on 2020-10-14 04:09

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201014_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location_point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326),
        ),
    ]
