from rest_framework import serializers
from .models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id','name','symbol','rank','price_usd','24h_volume_usd','market_cap_usd','available_supply','total_supply','percent_change_1h','percent_change_24h','percent_change_7d','last_updated')