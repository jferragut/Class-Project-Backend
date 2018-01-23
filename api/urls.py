from django.urls import include, path
from . import views

urlpatterns = [
    path('user/', views.User.as_view(), name='user'),
    path('user/watchlist', views.User.Watchlist.as_view(), name='watchlist'),
    path('user/alerts', views.User.Alerts.as_view(), name='alerts'),
    path('currencies/', views.Currencies.as_view(), name='currencies')
]