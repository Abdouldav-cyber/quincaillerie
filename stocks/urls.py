from django.urls import path
from . import views

urlpatterns = [
    path('mouvements/', views.liste_mouvements, name='liste_mouvements'),
    path('ajouter-stock/', views.ajouter_stock, name='ajouter_stock'),
    path('ajouter-mouvement/', views.ajouter_mouvement, name='ajouter_mouvement'),
]