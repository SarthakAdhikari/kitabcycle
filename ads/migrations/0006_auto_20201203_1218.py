# Generated by Django 3.1.3 on 2020-12-03 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_price_price_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ads.book'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='pictures',
            field=models.ImageField(blank=True, upload_to='ad_images'),
        ),
    ]
