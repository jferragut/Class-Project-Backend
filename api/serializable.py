from rest_framework import serializers
from .models import Currency
from .models import Alerts
from .models import UserWatchlist
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password', 'is_active', 'last_login','date_joined', 'email_contact','subscription_status')


class UserWatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWatchlist
        fields = ('currency_id','name','symbol','rank','price_usd','volume_24h_usd','market_cap_usd','available_supply','total_supply','percent_change_1h','percent_change_24h','percent_change_7d','last_updated')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('currency_id','name','symbol','rank','price_usd','volume_24h_usd','market_cap_usd','available_supply','total_supply','percent_change_1h','percent_change_24h','percent_change_7d','last_updated')

    