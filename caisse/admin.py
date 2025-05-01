from django.contrib import admin
from .models import TransactionCaisse, ClotureCaisse

@admin.register(TransactionCaisse)
class TransactionCaisseAdmin(admin.ModelAdmin):
    list_display = ('type_transaction', 'montant', 'date_creation', 'utilisateur')
    list_filter = ('type_transaction', 'date_creation')

@admin.register(ClotureCaisse)
class ClotureCaisseAdmin(admin.ModelAdmin):
    list_display = ('date_cloture', 'solde_ouverture', 'solde_cloture', 'utilisateur')
    list_filter = ('date_cloture',)
