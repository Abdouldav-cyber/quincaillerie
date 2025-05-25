# C:\Users\ASUS\Desktop\ProjetsDjango\quincaillerie\quincaillerie\clients\urls.py
from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.liste_clients, name='liste_clients'),
    path('ajouter/', views.ajouter_client, name='ajouter_client'),
    path('modifier/<int:pk>/', views.modifier_client, name='modifier_client'),
    path('ajouter-relance/<int:client_pk>/', views.ajouter_relance, name='ajouter_relance'),
    path('supprimer/<int:pk>/', views.supprimer_client, name='supprimer_client'),
]