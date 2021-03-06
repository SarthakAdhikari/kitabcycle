# Generated by Django 3.1.1 on 2020-10-14 03:51

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('bio', models.CharField(max_length=1000)),
                ('location_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('phone_number', models.BigIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
