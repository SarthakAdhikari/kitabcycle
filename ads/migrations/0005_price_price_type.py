# Generated by Django 3.1.3 on 2020-12-02 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_auto_20201202_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='price_type',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='ads.pricetype'),
            preserve_default=False,
        ),
    ]
