from django.urls import path
from . import views
app_name = 'fournisseurs'
urlpatterns = [
    path('', views.liste_fournisseurs, name='liste_fournisseurs'),
    path('ajouter/', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('modifier/<int:pk>/', views.modifier_fournisseur, name='modifier_fournisseur'),
    path('supprimer/<int:pk>/', views.supprimer_fournisseur, name='supprimer_fournisseur'),
]
