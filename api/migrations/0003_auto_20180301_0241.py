# Generated by Django 2.0.1 on 2018-03-01 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_currency_max_supply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='max_supply',
            field=models.CharField(default='N/A', max_length=20),
        ),
    ]