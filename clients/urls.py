from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_clients, name='liste_clients'),
    path('ajouter/', views.ajouter_client, name='ajouter_client'),
    path('modifier/<int:pk>/', views.modifier_client, name='modifier_client'),
    path('relance/<int:client_pk>/', views.ajouter_relance, name='ajouter_relance'),
]
