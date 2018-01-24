from rest_framework import status
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

#import models and serializer
from .models import Currency
from .serializable import CurrencySerializer


         
        
class User(APIView):
    def get(self, request, user_id):
        
        # look for the User in the database
        theUser = User.objects.get(pk=user_id)
        
        serializer = UserSerializer(theUser, many=False)
        return Response(serializer.data)
        
    def put(self, request):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        newUser = User(firstname=body['firstname'],lastname=body['lastname'],email=body['email'],password=body['password'],
                  email_contact=body['email_contact'],status=body['status'])
        newUser.save()
        
        serializer = UserSerializer(newUser, many=False)
        return Response(serializer.data)
        
    def post(self, request, user_id):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        # Look for the user in the database and update the properties 
        # based on what came from the request
        theUser = Game.objects.get(pk=game_id)
        theUser.firstname = body['firstname']
        theUser.lastname = body['lastname']
        theUser.email = body['email']
        theUser.password = body['password']
        theUser.email_contact = body['email_contact']
        theUser.status = body['status']
        theUser.save()
        
        # serialize the response object and pass it back
        serializer = UserSerializer(theUser, many=False)
        return Response(serializer.data)
        
    def delete(self, request, user_id):
        
        theUser = User.objects.get(pk=user_id)
        theUser.delete()
        
        return Response("ok")
        
        
class User.Watchlist(APIView):
    def get(self, request, currency_id):
        
        # look for the Watchlist Items in the database
        watchlistItem = User.Watchlist.objects.get(pk=currency_id)
        
        serializer = UserWatchlistSerializer(watchlistItem, many=False)
        return Response(serializer.data)
        
    def put(self, request):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        newWatchlistItem = User.Watchlist(currency_id=body['currency_id'],name=body['name'],symbol=body['symbol'],
                      rank=body['rank'],price_usd=body['price_usd'],24h_volume_usd=body['24h_volume_usd'],
                      market_cap_usd=body['market_cap_usd'],available_supply=body['available_supply'],
                      total_supply=body['total_supply'],percent_change_1h=body['percent_change_1h'],
                      percent_change_24h=body['percent_change_24h'],percent_change_7d=body['percent_change_7d'],last_updated=body['last_updated'])
        newWatchlistItem.save()
        
        serializer = UserWatchlistSerializer(newWatchlistItem, many=False)
        return Response(serializer.data)
        
    def post(self, request, user_id):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        # Look for the user in the database and update the properties 
        # based on what came from the request
        watchlistItem = User.Watchlist.objects.get(pk=currency_id)
        watchlistItem.currency_id = body['currency_id']
        watchlistItem.name = body['name']
        watchlistItem.rank = body['rank']
        watchlistItem.price_usd = body['price_usd']
        watchlistItem.24h_volume_usd = body['24h_volume_usd']
        watchlistItem.market_cap_usd = body['market_cap_usd']
        watchlistItem.available_supply = body['available_supply']
        watchlistItem.total_supply = body['total_supply']
        watchlistItem.percent_change_1h = body['percent_change_1h']
        watchlistItem.percent_change_24h = body['percent_change_24h']
        watchlistItem.percent_change_7d = body['percent_change_7d']
        watchlistItem.last_updated = body['last_updated']
        watchlistItem.save()
        
        # serialize the response object and pass it back
        serializer = UserWatchlistSerializer(watchlistItem, many=False)
        return Response(serializer.data)
        
    def delete(self, request, currency_id):
        
        watchlistItem = User.Watchlist.objects.get(pk=currency_id)
        watchlistItem.delete()
        
        return Response("ok")
        
        
        
class Currencies(APIView):
    def get(self, request, game_id):
        
        # look for the currency in the database
        singleCurrency = Currency.objects.get(pk=currency_id)
        
        serializer = CurrencySerializer(singleCurrency, many=False)
        return Response(serializer.data)
        
    def put(self, request):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        newCurrency = Currency(currency_id=body['currency_id'],name=body['name'],symbol=body['symbol'],
                      rank=body['rank'],price_usd=body['price_usd'],24h_volume_usd=body['24h_volume_usd'],
                      market_cap_usd=body['market_cap_usd'],available_supply=body['available_supply'],
                      total_supply=body['total_supply'],percent_change_1h=body['percent_change_1h'],
                      percent_change_24h=body['percent_change_24h'],percent_change_7d=body['percent_change_7d'],last_updated=body['last_updated'])
        newCurrency.save()
        
        serializer = CurrencySerializer(newCurrency, many=False)
        return Response(serializer.data)
        
    def post(self, request, game_id):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        # Look for the game in the database and update the properties 
        # based on what came from the request
        singleCurrency = Currency.objects.get(pk=currency_id)
        singleCurrency.currency_id = body['currency_id']
        singleCurrency.name = body['name']
        singleCurrency.rank = body['rank']
        singleCurrency.price_usd = body['price_usd']
        singleCurrency.24h_volume_usd = body['24h_volume_usd']
        singleCurrency.market_cap_usd = body['market_cap_usd']
        singleCurrency.available_supply = body['available_supply']
        singleCurrency.total_supply = body['total_supply']
        singleCurrency.percent_change_1h = body['percent_change_1h']
        singleCurrency.percent_change_24h = body['percent_change_24h']
        singleCurrency.percent_change_7d = body['percent_change_7d']
        singleCurrency.last_updated = body['last_updated']
        singleCurrency.save()
        
        # serialize the response object and pass it back
        serializer = CurrencySerializer(singleCurrency, many=False)
        return Response(serializer.data)
        
    def delete(self, request, currency_id):
        
        singleCurrency = Currency.objects.get(pk=currency_id)
        singleCurrency.delete()
        
        return Response("ok")