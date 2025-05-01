from django.contrib import admin
from .models import Stock, MouvementStock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('produit', 'quantite', 'seuil_critique', 'emplacement', 'produit_code_barres')
    list_filter = ('produit__categorie', 'seuil_critique', 'emplacement')
    search_fields = ('produit__nom', 'emplacement', 'produit__code_barres')

    def produit_code_barres(self, obj):
        return obj.produit.code_barres
    produit_code_barres.short_description = 'Code-barres'

@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin):
    list_display = ('produit', 'quantite', 'type_mouvement', 'date_mouvement', 'raison')
    list_filter = ('type_mouvement', 'date_mouvement')
    search_fields = ('produit__nom', 'raison')

    def produit_code_barres(self, obj):
        return obj.produit.code_barres
    produit_code_barres.short_description = 'Code-barres'