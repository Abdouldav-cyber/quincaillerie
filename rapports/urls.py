from django.urls import path
from . import views

urlpatterns = [
    path('stocks/', views.rapport_stocks, name='rapport_stocks'),
    path('exporter-stocks-csv/', views.exporter_stocks_csv, name='exporter_stocks_csv'),
    path('ventes/', views.rapport_ventes, name='rapport_ventes'),
    path('exporter-ventes-csv/', views.exporter_ventes_csv, name='exporter_ventes_csv'),
    path('financier/', views.rapport_financier, name='rapport_financier'),
    path('exporter-financier-csv/', views.exporter_financier_csv, name='exporter_financier_csv'),
]