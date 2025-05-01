# quincaillerie/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='accueil.html'), name='accueil'),
    path('produits/', include('produits.urls')),
    path('stocks/', include('stocks.urls')),
    path('achats/', include('achats.urls')),
    path('ventes/', include('ventes.urls')),
    path('clients/', include('clients.urls')),
    path('fournisseurs/', include('fournisseurs.urls')),
    path('caisse/', include('caisse.urls')),
    path('rapports/', include('rapports.urls')),
    path('utilisateurs/', include('utilisateurs.urls')),
    path('login/', LoginView.as_view(template_name='utilisateurs/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='accueil'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)