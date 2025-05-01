from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_stocks, name='liste_stocks'),
    path('ajouter/', views.ajouter_stock, name='ajouter_stock'),
    path('modifier/<int:pk>/', views.modifier_stock, name='modifier_stock'),
    path('mouvement/ajouter/', views.ajouter_mouvement_stock, name='ajouter_mouvement_stock'),
]
