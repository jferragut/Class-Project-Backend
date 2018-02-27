import json
import requests
from rest_framework import permissions, routers, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .utils import ObjectNotFound
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib import admin
admin.autodiscover()

#import models and serializer
from api.models import Currency, ExtendUser
from django.contrib.auth.models import User
from .serializable import CurrencySerializer, UserSerializer


         
#------------------------------------------------
#Begin Views for User        
#------------------------------------------------
        
class UserView(APIView):
    
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # Get method that will return a given user's information
    def get(self, request, user_name):
        
        try:

            # look for the User in the database
            theUser = User.objects.get(username=user_name)
            
            # Custom Error Handling
            
        except User.DoesNotExist:
            # Custom error message to return if user is not found
            raise ObjectNotFound("Could not find the user, "+str(user_name)+".")

        # Serialize the response object and pass it back
        serializer = UserSerializer(theUser, many=False)
        
        # Return the user object
        return Response(serializer.data)
        
        
    # Put method that will add a new user into the database
    def put(self, request):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        # Define what the prototype is for a user and grab data from the dictionary
        newUser = User(username=body['username'],first_name=body['first_name'],last_name=body['last_name'],email=body['email'],
        password=body['password'],is_active=body['is_active'])

        try:
            # Save the new user
            newUser.save()
            
        except Exception as e:

            raise ObjectNotFound("Could not save the User {}".format(e))

        # Serialize the response object and pass it back
        serializer = UserSerializer(newUser, many=False)

        # Return the new user object
        return Response(serializer.data)
    
    
    # Post method for updating a user record in the database
    def post(self, request, user_name):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        # Look for the user in the database and update the properties 
        # based on what came from the request
        theUser = User.objects.get(username=user_name)
        theUser.username = body['username']
        theUser.first_name = body['first_name']
        theUser.last_name = body['last_name']
        theUser.email = body['email']
        theUser.password = body['password']
        theUser.is_active = body['is_active']
        theUser.extenduser.email_contact = body['email_contact']
        theUser.extenduser.subscription_status = body['subscription_status']
        
        try:
            # Save the new user
            theUser.save()
        
        except Exception as e:

            raise ObjectNotFound("Could not save the User {}".format(e))
        
        # Serialize the response object and pass it back
        serializer = UserSerializer(theUser, many=False)
        return Response(serializer.data)
        
    def delete(self, request, user_name):
        
        try:
            # Find the user and get their record
            theUser = User.objects.get(username=user_name)
    
            # Custom Error Handling
            
        except User.DoesNotExist:
            # Custom error message to return if user is not found
            raise ObjectNotFound("Could not find the user, "+str(user_name)+".")
        
        # Delete the user record
        theUser.delete()
        
        # Return a response
        return Response("Removed user,"+user_name+".")
      
      
#------------------------------------------------
#Begin Views for User Watchlist        
#------------------------------------------------

class UserWatchlistDetailView(APIView):
    
    # Get method that will return a specific user's watchlist
    def get(self, request, user_name):
        
        # Look for the User in the database
        theUser = User.objects.get(username=user_name)
        
        # Grab the user's watchlist
        theWatchlist = theUser.extenduser.watchlist.all()
        
        # Serialize the data using the currency serializer because it's an array
        # of currency objects
        serializer = CurrencySerializer(theWatchlist, many=True)
        
        # Return the array of objects
        return Response(serializer.data)        
        
        
class UserWatchlistView(APIView):
    
    # Put method that will add a currency to a user's watchlist
    def put(self, request, user_name, coin_symbol):
        
        try:
            # Get the user's watchlist
            theUser = User.objects.get(username=user_name)
            
            # Get the coin specified in the query
            theCoin = Currency.objects.get(symbol=coin_symbol)
            
            # Add the coin to the watchlist
            theUser.extenduser.watchlist.add(theCoin)
            
        #Custom Error Handling
        except User.DoesNotExist:
            # Custom error message to return if user is not found
            raise ObjectNotFound("Could not find the user, "+str(user_name)+".")
            
        except Currency.DoesNotExist:
            # Custom error message to return if coin is not found
            raise ObjectNotFound("Could not find the currency, "+str(coin_symbol)+".")
        
        newWatchlist = theUser.extenduser.watchlist.all()
        
        # Serialize the currency data    
        serializer = CurrencySerializer(newWatchlist, many=True)
        
        # Return the object
        return Response(serializer.data)
        
    def delete(self, request, user_name, coin_symbol):
        
        try:
            # get watchlist for given user        
            theUser = User.objects.get(username=user_name)
            
            # get the coin specified in the query
            theCoin = Currency.objects.get(symbol=coin_symbol)
        
        #Custom Error Handling
        except User.DoesNotExist:
            # Custom error message to return if user is not found
            raise ObjectNotFound("Could not find the user, "+str(user_name)+".")
            
        except Currency.DoesNotExist:
            # Custom error message to return if coin is not found
            raise ObjectNotFound("Could not find the currency, "+str(coin_symbol)+".")
        
        # Remove the coin from watchlist
        theUser.extenduser.watchlist.remove(theCoin)
        
        newWatchlist = theUser.extenduser.watchlist.all()
        
        # Serialize the currency data    
        serializer = CurrencySerializer(newWatchlist, many=True)
        
        # Return the object
        return Response(serializer.data)
        
        
#------------------------------------------------
# Begin Views for Currency 
#------------------------------------------------

class CurrencyView(APIView):
    
    # Get method that will return a single coin
    def get(self, request, symbol):
        try:
            # Look for the coin in the database
            singleCurrency = Currency.objects.get(symbol=symbol)
        
        except Exception as e:
            # Custom error message to return if coin could not be updated
            raise ObjectNotFound("Could not find the currency {}".format(e))
        
        # Serialize the coin
        serializer = CurrencySerializer(singleCurrency, many=False)
        
        # Return the coin
        return Response(serializer.data)
    
    # Put method that will create a new coin
    def put(self, request):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        try:
            # Define what the prototype is for a user and grab data from the dictionary
            newCurrency = Currency(name=body['name'],symbol=body['symbol'],
                          rank=body['rank'],price_usd=body['price_usd'],volume_24h_usd=body['volume_24h_usd'],
                          market_cap_usd=body['market_cap_usd'],available_supply=body['available_supply'],
                          total_supply=body['total_supply'],percent_change_1h=body['percent_change_1h'],
                          percent_change_24h=body['percent_change_24h'],percent_change_7d=body['percent_change_7d'],
                          last_updated=body['last_updated'],ticker_history=body['ticker_history'])
            
            # Save the new coin
            newCurrency.save()
        
        except Exception as e:
            # Custom error message to return if coin could not be created
            raise ObjectNotFound("Could not create the coin {}".format(e))
            
        
        # Serialize the new coin data
        serializer = CurrencySerializer(newCurrency, many=False)
        
        # Return the coin
        return Response(serializer.data)
    
    # Post method that will update a coin that already exists
    def post(self, request, symbol):
        
        # I get the content from the body request and convert it into a dictionary
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        try:
            # Look for the game in the database and update the properties 
            # based on what came from the request
            singleCurrency = Currency.objects.get(symbol=symbol)
            
        except Currency.DoesNotExist:
            # Custom error message to return if coin is not found
            raise ObjectNotFound("Could not find the currency, "+str(symbol)+".")
            
        try:    
            #define and map the prototype
            singleCurrency.name = body['name']
            singleCurrency.symbol = body['symbol']
            singleCurrency.rank = body['rank']
            singleCurrency.price_usd = body['price_usd']
            singleCurrency.volume_24h_usd = body['volume_24h_usd']
            singleCurrency.market_cap_usd = body['market_cap_usd']
            singleCurrency.available_supply = body['available_supply']
            singleCurrency.total_supply = body['total_supply']
            singleCurrency.percent_change_1h = body['percent_change_1h']
            singleCurrency.percent_change_24h = body['percent_change_24h']
            singleCurrency.percent_change_7d = body['percent_change_7d']
            
            # Save the updates
            singleCurrency.save()
            
        except Exception as e:
            # Custom error message to return if coin could not be updated
            raise ObjectNotFound("Could not update the coin data {}".format(e))

        
        # serialize the response object and pass it back
        serializer = CurrencySerializer(singleCurrency, many=False)
        return Response(serializer.data)
    
    # Delete method that will remove a currency from the database
    def delete(self, request, symbol):
        
        try:
            # Find the currency in the database
            singleCurrency = Currency.objects.get(symbol=symbol)
        
        except Currency.DoesNotExist:
            # Custom error message to return if coin is not found
            raise ObjectNotFound("Could not find the currency, "+str(symbol)+".")
            
        try:    
            # Delete the selected currency    
            singleCurrency.delete()
        
        except Exception as e:
            # Custom error message to return if coin cannot be deleted
            raise ObjectNotFound("Could not delete the coin {}".format(e))
            
        # Send response
        return Response("Removed currency,"+symbol+".")
        

class CurrenciesView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # Get method that will return a list of all currencies in the database
    def get(self, request):
        
        try:
            # look for the currency in the database
            listCurrencies = Currency.objects.all()
        
        except Exception as e:
            # Custom error message to return if no coins exist
            raise ObjectNotFound("No currencies exist. {}".format(e))
        
        # Serialize the response
        serializer = CurrencySerializer(listCurrencies, many=True)
        
        # Return the array of currency objects
        return Response(serializer.data)


        
#------------------------------------------------
# Begin Views for Alerts 
#------------------------------------------------

class AlertsView(APIView):
    
    # Get method that returns all coins that the user is being alerted for
    def get(self, request, user_name):
        
        try:
            # look for the User in the database
            theUser = User.objects.get(username=user_name)
            
        except Exception as e:
            # Custom error message to return if user cannot be found
            raise ObjectNotFound("Could not find the user. {}".format(e))
            
        try:    
            # Look for the alert in the database
            getAlerts = theUser.extenduser.alerts.all()
        
        except Exception as e:
            # Custom error message to return if user does not have alerts
            raise ObjectNotFound("Could not find user alerts. {}".format(e))
        
        
        # Serialize the response
        serializer = CurrencySerializer(getAlerts, many=True)
        
        # Return the list of alerts
        return Response(serializer.data)
        
class UpdateAlertsView(APIView):
    
    # Put method that will add a currency to a user's watchlist
    def put(self, request, user_name, coin_symbol):
        
        try:
            # Get the user's watchlist
            theUser = User.objects.get(username=user_name)
            
            # Get the coin specified in the query
            theCoin = Currency.objects.get(symbol=coin_symbol)
            
            # Add the coin to the user's alerts
            theUser.extenduser.alerts.add(theCoin)
            
            
        #Custom Error Handling
        except User.DoesNotExist:
            # Custom error message to return if user is not found
            raise ObjectNotFound("Could not find the user, "+str(user_name)+".")
            
        except Currency.DoesNotExist:
            # Custom error message to return if coin is not found
            raise ObjectNotFound("Could not find the currency, "+str(coin_symbol)+".")
            
        
        # Serialize the currency data    
        serializer = CurrencySerializer(theCoin, many=False)
        
        # Return the object
        return Response(serializer.data)
    
    
    # Delete method to remove an alert from a user    
    def delete(self, request, user_name, coin_symbol):
        
        try:
            # get watchlist for given user        
            theUser = User.objects.get(username=user_name)
            
            # get the coin specified in the query
            theCoin = Currency.objects.get(symbol=coin_symbol)
        
            # Remove the coin from watchlist
            theUser.extenduser.alerts.remove(theCoin)
            
            
        #Custom Error Handling
        except User.DoesNotExist:
            # Custom error message to return if user is not found
            raise ObjectNotFound("Could not find the user, "+str(user_name)+".")
            
        except Currency.DoesNotExist:
            # Custom error message to return if coin is not found
            raise ObjectNotFound("Could not find the currency, "+str(coin_symbol)+".")
        
        
        # Send response
        return Response("Removed currency,"+coin_symbol+" from alerts.")



#------------------------------------------------
# Begin View for Reddit Request 
#------------------------------------------------

class RedditView(APIView):
    
    # Get method that returns a subreddit to embed based upon
    def get(self, request, coin):
        
        try:
            # create the URL for the request
            url = "https://www.reddit.com/r/%s.json" % (coin)
            # setup the request
            r = requests.get(url)
            
        except Exception as e:
            # Custom error message to return if request cannot be processed
            raise ObjectNotFound("Could not process the request. {}".format(e))
            
        # Return the json object
        return Response(r)

