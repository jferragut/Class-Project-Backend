from django.urls import include, path
from . import views

urlpatterns = [
    #Request specific user information (GET), Update a specific user (POST), or Remove a specific user (DELETE)
    path('user/<str:user_name>', views.UserView.as_view()), 
    
    #Update a specific user's password(POST)
    path('user/<str:user_name/cp>', views.UserPasswordChangeView.as_view()), 
    
    #Create a new user (PUT)
    path('user/', views.UserView.as_view()), 
    
    #add coin to Watchlist(PUT) or Delete from Watchlist(DELETE)
    path('user/<str:user_name>/watchlist/<str:coin_symbol>', views.UserWatchlistView.as_view()),
    
    #Request user's Watchlist (GET)
    path('user/<str:user_name>/watchlist', views.UserWatchlistDetailView.as_view()), 
    
    #Add (PUT) or Delete currency(DELETE) from Alerts
    path('user/<str:user_name>/alert/<str:coin_symbol>', views.UpdateAlertsView.as_view()), 
    
    #Request user Alerts (GET)
    path('user/<str:user_name>/alert', views.AlertsView.as_view()),
    
    #Request an individual currency's information(GET), update (POST), or delete (DELETE) a currency from the database
    path('currency/<str:symbol>', views.CurrencyView.as_view()),
    
    #Add a new currency (PUT)
    path('currency/', views.CurrencyView.as_view()),
    
    #Request a list of all currencies
    path('currencies/', views.CurrenciesView.as_view()),
    
    path('email/', views.EmailsView.as_view()),
    
]