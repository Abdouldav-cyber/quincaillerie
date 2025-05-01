from django.contrib import admin
from .models import Produit, Categorie

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'prix_vente', 'code_barres')
    list_filter = ('categorie',)
    search_fields = ('nom', 'code_barres')

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)