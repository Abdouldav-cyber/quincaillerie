from django.contrib import admin
from .models import Stock, MouvementStock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('produit', 'quantite', 'seuil_critique', 'emplacement')
    list_filter = ('produit__categorie',)
    search_fields = ('produit__nom',)

@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin):
    list_display = ('stock', 'type_mouvement', 'quantite', 'date_creation')
    list_filter = ('type_mouvement',)
