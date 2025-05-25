# stocks/urls.py
from django.urls import path
from . import views

app_name = 'stocks'

urlpatterns = [
    path('', views.liste_mouvements, name='liste_mouvements'),
    path('stocks/', views.liste_stocks, name='liste_stocks'),
    path('ajouter-stock/', views.ajouter_stock, name='ajouter_stock'),
    path('ajouter-mouvement/', views.ajouter_mouvement, name='ajouter_mouvement'),
    path('modifier-stock/<int:pk>/', views.modifier_stock, name='modifier_stock'),
]