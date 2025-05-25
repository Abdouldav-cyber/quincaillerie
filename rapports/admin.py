from django.contrib import admin
from .models import Stock, Vente

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['produit', 'quantite', 'seuil_critique', 'emplacement']
    list_filter = ['emplacement']
    search_fields = ['produit__nom', 'emplacement']

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ['produit', 'quantite', 'prix_unitaire', 'date_vente', 'client']
    list_filter = ['date_vente']
    search_fields = ['produit__nom', 'client']