from django.urls import path
from . import views
app_name = 'ventes'
urlpatterns = [
    path('', views.liste_ventes, name='liste_ventes'),
    path('ajouter/', views.ajouter_vente, name='ajouter_vente'),
    path('ticket/<int:pk>/', views.voir_ticket_vente, name='voir_ticket_vente'),
]