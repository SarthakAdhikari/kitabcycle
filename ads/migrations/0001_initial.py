# Generated by Django 3.1.1 on 2020-10-28 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ad types')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ad types')),
                ('ISBN', models.CharField(max_length=13, verbose_name='ISBN')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_price', models.FloatField(verbose_name='Current Price')),
                ('original_price', models.FloatField(verbose_name='Original Price')),
            ],
        ),
        migrations.CreateModel(
            name='PriceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Price type')),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('pictures', models.ImageField(upload_to='ad_images')),
                ('ad_type', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ads.adtypes')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ads.book')),
                ('price', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ads.price')),
            ],
        ),
    ]
