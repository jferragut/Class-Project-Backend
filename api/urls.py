from django.urls import include, path
from . import views

urlpatterns = [
    path('games/', views.GamesView.as_view(), name='games'),
    path('clean/', views.GamesView.as_view(), name='games'),
    path('game/', views.GameView.as_view(), name='game'),
    path('game/<int:game_id>', views.GameView.as_view(), name='game'),
]