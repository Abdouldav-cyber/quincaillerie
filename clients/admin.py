from django.contrib import admin
from .models import Client, Relance

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'solde')
    search_fields = ('nom', 'email')

@admin.register(Relance)
class RelanceAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_relance', 'est_automatique')
    list_filter = ('est_automatique',)
