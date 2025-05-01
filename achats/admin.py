from django.contrib import admin
from .models import CommandeAchat, ArticleAchat

@admin.register(CommandeAchat)
class CommandeAchatAdmin(admin.ModelAdmin):
    list_display = ('fournisseur', 'date_commande', 'statut', 'montant_paye')
    list_filter = ('statut', 'fournisseur')
    search_fields = ('fournisseur__nom', 'facture')

@admin.register(ArticleAchat)
class ArticleAchatAdmin(admin.ModelAdmin):
    list_display = ('commande', 'produit', 'quantite', 'prix_unitaire')
    search_fields = ('produit__nom',)
