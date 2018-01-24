from django.db import models

# Create your models here.
class Currency(models.Model):
    currency_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=7)
    rank = models.CharField(max_length=5)
    price_usd = models.CharField(max_length=20)
    24h_volume_usd = models.CharField(max_length=20)
    market_cap_usd = models.CharField(max_length=20)
    available_supply = models.CharField(max_length=20)
    total_supply = models.CharField(max_length=20)
    percent_change_1h = models.CharField(max_length=20)
    percent_change_24h = models.CharField(max_length=20)
    percent_change_7d = models.CharField(max_length=20)
    last_updated = models.CharField(max_length=20)
