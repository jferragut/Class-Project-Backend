from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


#ExtendUser will extend the user model
class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    email_contact = models.BooleanField(default=True)
    subscription_status = models.BooleanField(default=False)
    
@receiver(post_save, sender=User)
def create_user_ExtendUser(sender, instance, created, **kwargs):
    if created:
        ExtendUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_ExtendUser(sender, instance, **kwargs):
    instance.extenduser.save()



class UserWatchlist(models.Model):
    currency_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=7)
    rank = models.CharField(max_length=5)
    price_usd = models.CharField(max_length=20)
    volume_24h_usd = models.CharField(max_length=20)
    market_cap_usd = models.CharField(max_length=20)
    available_supply = models.CharField(max_length=20)
    total_supply = models.CharField(max_length=20)
    percent_change_1h = models.CharField(max_length=20)
    percent_change_24h = models.CharField(max_length=20)
    percent_change_7d = models.CharField(max_length=20)
    last_updated = models.CharField(max_length=20)
    

class Currency(models.Model):
    currency_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=7)
    rank = models.CharField(max_length=5)
    price_usd = models.FloatField(max_length=20)
    volume_24h_usd = models.CharField(max_length=20)
    market_cap_usd = models.CharField(max_length=20)
    available_supply = models.CharField(max_length=20)
    total_supply = models.CharField(max_length=20)
    percent_change_1h = models.CharField(max_length=20)
    percent_change_24h = models.CharField(max_length=20)
    percent_change_7d = models.CharField(max_length=20)
    last_updated = models.CharField(max_length=20)


class Alert(models.Model):
    currency_id = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    symbol = models.CharField(max_length=7)
    price_usd = models.FloatField(max_length=20)
    percent_change_1h = models.FloatField(max_length=20)
    percent_change_24h = models.FloatField(max_length=20)
    alert = models.CharField(max_length=20)
    
