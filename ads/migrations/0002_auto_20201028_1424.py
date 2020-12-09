# Generated by Django 3.1.1 on 2020-10-28 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ad type')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='ad_type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ads.adtype'),
        ),
        migrations.DeleteModel(
            name='AdTypes',
        ),
    ]
