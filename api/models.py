from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=15)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    email_contact = models.CharField(max_length=5)
    status = models.CharField(max_length=20)


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
    price_usd = models.CharField(max_length=20)
    volume_24h_usd = models.CharField(max_length=20)
    market_cap_usd = models.CharField(max_length=20)
    available_supply = models.CharField(max_length=20)
    total_supply = models.CharField(max_length=20)
    percent_change_1h = models.CharField(max_length=20)
    percent_change_24h = models.CharField(max_length=20)
    percent_change_7d = models.CharField(max_length=20)
    last_updated = models.CharField(max_length=20)

