# C:\Users\ASUS\Desktop\ProjetsDjango\quincaillerie\quincaillerie\rapports\urls.py
from django.urls import path
from . import views

app_name = 'rapports'

urlpatterns = [
    path('financier/', views.rapport_financier, name='rapport_financier'),
    path('financier/exporter-csv/', views.exporter_financier_csv, name='exporter_financier_csv'),
    path('stocks/', views.rapport_stocks, name='rapport_stocks'),
    path('stocks/exporter-csv/', views.exporter_stocks_csv, name='exporter_stocks_csv'),
    path('ventes/', views.rapport_ventes, name='rapport_ventes'),
    path('ventes/exporter-csv/', views.exporter_ventes_csv, name='exporter_ventes_csv'),
]