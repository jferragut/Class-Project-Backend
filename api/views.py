from rest_framework import status
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Game
from .serializable import GameSerializer

def hello(self):
    return HttpResponse("<h1>Hello</h1>")
    
def transactions(request, user_id):
    return HttpResponse("<h1>Here are the transactions for the user "+user_id+"</h1>")
    

class GamesView(APIView):
    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
         
        
class GameView(APIView):
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