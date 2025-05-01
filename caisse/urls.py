from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_caisse, name='liste_caisse'),
     path('transaction/ajouter/', views.ajouter_transaction_caisse, name='ajouter_transaction_caisse'),
     path('cloture/ajouter/', views.ajouter_cloture_caisse, name='ajouter_cloture_caisse'),
]
