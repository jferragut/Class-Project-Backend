from rest_framework import status
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

#import models and serializer
from .models import Currency
from .serializable import CurrencySerializer


         
        
class User(APIView):
    def get(self, request, game_id):
        
        # look for the game in the database
        singleGame = Game.objects.get(pk=game_id)
        
        serializer = GameSerializer(singleGame, many=False)
        return Response(serializer.data)
        
    def put(self, request):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        newGame = Game(player1=body['player1'], player2=body['player2'], winner=body['winner'])
        newGame.save()
        
        serializer = GameSerializer(newGame, many=False)
        return Response(serializer.data)
        
    def post(self, request, game_id):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        # Look for the game in the database and update the properties 
        # based on what came from the request
        singleGame = Game.objects.get(pk=game_id)
        singleGame.player1 = body['player1']
        singleGame.player2 = body['player2']
        singleGame.winner = body['winner']
        singleGame.save()
        
        # serialize the response object and pass it back
        serializer = GameSerializer(singleGame, many=False)
        return Response(serializer.data)
        
    def delete(self, request, game_id):
        
        singleGame = Game.objects.get(pk=game_id)
        singleGame.delete()
        
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
        singleGame = Game.objects.get(pk=game_id)
        singleGame.player1 = body['player1']
        singleGame.player2 = body['player2']
        singleGame.winner = body['winner']
        singleGame.save()
        
        # serialize the response object and pass it back
        serializer = GameSerializer(singleGame, many=False)
        return Response(serializer.data)
        
    def delete(self, request, currency_id):
        
        singleCurrency = Currency.objects.get(pk=currency_id)
        singleCurrency.delete()
        
        return Response("ok")