# Generated by Django 2.0.1 on 2018-01-30 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180130_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='ticker_history',
            field=models.CharField(default='', max_length=44),
        ),
    ]