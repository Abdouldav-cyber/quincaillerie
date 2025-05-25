from django.urls import path
from . import views

urlpatterns = [
    path('stocks/', views.rapport_stocks, name='rapport_stocks'),
    path('stocks/export/', views.exporter_stocks_csv, name='exporter_stocks_csv'),
    path('ventes/', views.rapport_ventes, name='rapport_ventes'),
    path('ventes/export/', views.exporter_ventes_csv, name='exporter_ventes_csv'),
    path('financier/', views.rapport_financier, name='rapport_financier'),
    path('financier/export/', views.exporter_financier_csv, name='exporter_financier_csv'),
]