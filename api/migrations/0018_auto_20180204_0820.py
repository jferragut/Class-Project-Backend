# Generated by Django 2.0.1 on 2018-02-04 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20180204_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='alerts',
            field=models.ManyToManyField(default='', related_name='extenduser_alerts', to='api.Currency'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ExtendUser'),
        ),
        migrations.AlterField(
            model_name='extenduser',
            name='watchlist',
            field=models.ManyToManyField(default='', related_name='extenduser_watchlist', to='api.Currency'),
        ),
    ]