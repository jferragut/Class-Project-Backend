from django.urls import include, path
from . import views

urlpatterns = [
    #Request user information (GET)
    path('user/<str:user_name>', views.UserView.as_view()), 
    
    #Request user information (GET)
    path('user/', views.UserView.as_view()), 
    
    #add coin to Watchlist(PUT) or Delete from Watchlist(DELETE)
    path('user/<str:user_name>/watchlist/<str:coin_symbol>', views.UserWatchlistView.as_view()),
    
    #Request user's Watchlist (GET)
    path('user/<str:user_name>/watchlist', views.UserWatchlistDetailView.as_view()), 
    
    #Add (PUT) or Delete currency(DELETE) from Alerts
    path('user/<str:user_name>/alert/<str:coin_symbol>', views.UpdateAlertsView.as_view()), 
    
    #Request user Alerts (GET)
    path('user/<str:user_name>/alert', views.AlertsView.as_view()),
    
    #Request an individual currency's information(GET), Add (PUT), update (POST), or delete (DELETE) a currency from the database
    path('currency/<int:currency_id>', views.CurrencyView.as_view()),
    
    #Request a list of all currencies
    path('currencies/', views.CurrenciesView.as_view()),
]