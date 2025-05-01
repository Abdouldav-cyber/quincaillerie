from django.urls import path
from . import views

urlpatterns = [
    path('ventes/', views.rapport_ventes, name='rapport_ventes'),
    path('stocks/', views.rapport_stocks, name='rapport_stocks'),
    path('financier/', views.rapport_financier, name='rapport_financier'),
    path('ventes/exporter/csv/', views.exporter_ventes_csv, name='exporter_ventes_csv'),
    path('ventes/exporter/pdf/', views.exporter_ventes_pdf, name='exporter_ventes_pdf'),
    path('ventes/exporter/excel/', views.exporter_ventes_excel, name='exporter_ventes_excel'),
    path('stocks/exporter/csv/', views.exporter_stocks_csv, name='exporter_stocks_csv'),
]