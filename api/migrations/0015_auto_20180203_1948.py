# Generated by Django 2.0.1 on 2018-02-03 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20180203_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='email_contact',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='subscription_status',
            field=models.BooleanField(default=True),
        ),
    ]