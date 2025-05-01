from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('ajouter/', views.ajouter_utilisateur, name='ajouter_utilisateur'),
    path('modifier/<int:pk>/', views.modifier_utilisateur, name='modifier_utilisateur'),
    path('connexion/', LoginView.as_view(template_name='utilisateurs/connexion.html'), name='login'),
    path('deconnexion/', LogoutView.as_view(next_page='accueil'), name='logout'),
]