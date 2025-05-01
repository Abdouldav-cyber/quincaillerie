from django.contrib import admin
from .models import Stock, Vente

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('produit', 'quantite', 'seuil_critique', 'emplacement', 'produit_code_barres')
    list_filter = ('produit__categorie', 'seuil_critique', 'emplacement')
    search_fields = ('produit__nom', 'emplacement', 'produit__code_barres')

    def produit_code_barres(self, obj):
        return obj.produit.code_barres
    produit_code_barres.short_description = 'Code-barres'

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ('produit', 'quantite', 'prix_unitaire', 'client', 'date_vente', 'produit_code_barres')
    list_filter = ('produit__categorie', 'date_vente')
    search_fields = ('produit__nom', 'client', 'produit__code_barres')

    def produit_code_barres(self, obj):
        return obj.produit.code_barres
    produit_code_barres.short_description = 'Code-barres'