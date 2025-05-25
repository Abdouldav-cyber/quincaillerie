from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_achats, name='liste_achats'),
    path('ajouter/', views.ajouter_achat, name='ajouter_achat'),
    path('modifier/<int:pk>/', views.modifier_achat, name='modifier_achat'),
]