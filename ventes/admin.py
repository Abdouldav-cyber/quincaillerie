from django.contrib import admin
from .models import Vente, ArticleVente

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_vente', 'client', 'montant_total', 'est_credit')
    list_filter = ('est_credit', 'date_vente')
    search_fields = ('client__nom',)

@admin.register(ArticleVente)
class ArticleVenteAdmin(admin.ModelAdmin):
    list_display = ('vente', 'produit', 'quantite', 'prix_unitaire')
    search_fields = ('produit__nom',)
