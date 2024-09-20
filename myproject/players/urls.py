# players/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.players_list, name='players'),  # Seznam hráčů
    path('add/', views.add_player, name='add_player'),  # Přidání hráče
    path('<int:pk>/', views.player_detail, name='player_detail'),  # Detail hráče
    path('delete/<int:pk>/', views.delete_player, name='delete_player'),  # Smazání hráče
    path('update/<int:pk>/', views.update_player, name='update_player'),  # Aktualizace hráče
]
