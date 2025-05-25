from django.contrib import admin
from .models import MouvementStock

@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin):
    list_display = ['produit', 'quantite', 'type_mouvement', 'date_mouvement', 'description']
    list_filter = ['type_mouvement', 'date_mouvement']
    search_fields = ['produit__nom', 'description']