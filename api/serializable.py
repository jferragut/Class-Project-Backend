from rest_framework import serializers
from .models import Currency
from .models import User
from .models import UserWatchlist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('firstname','lastname','email','password','email_contact','status')


class UserWatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWatchlist
        fields = ('currency_id','name','symbol','rank','price_usd','volume_24h_usd','market_cap_usd','available_supply','total_supply','percent_change_1h','percent_change_24h','percent_change_7d','last_updated')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('currency_id','name','symbol','rank','price_usd','volume_24h_usd','market_cap_usd','available_supply','total_supply','percent_change_1h','percent_change_24h','percent_change_7d','last_updated')

    