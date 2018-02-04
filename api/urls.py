from django.urls import include, path
from . import views

urlpatterns = [
    path('user/<str:user_name>', views.UserView.as_view()),
    path('user/<str:user_name>/watchlist/<str:coin_symbol>', views.UserWatchlistView.as_view()),
    path('user/<str:user_name>/watchlist', views.UserWatchlistDetailView.as_view()),
    path('user/<str:user_name>/alert', views.AlertsView.as_view()),
    path('currency/<int:currency_id>', views.CurrencyView.as_view()),
    path('currencies/', views.CurrenciesView.as_view()),
    path('currencies/<str:user_name>', views.CurrenciesView.as_view())
]