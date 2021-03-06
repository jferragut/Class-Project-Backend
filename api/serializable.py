from rest_framework import serializers
from .models import Currency,ExtendUser, CoinAlert
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','password', 'is_active', 'last_login','date_joined')

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('name','symbol','rank','price_usd','volume_24h_usd','market_cap_usd','available_supply','total_supply','percent_change_1h','percent_change_24h','percent_change_7d','last_updated','ticker_history')

class CoinAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinAlert
        fields = ('coin','alert_type')

    

    