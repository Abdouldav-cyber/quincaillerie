# utilisateurs/admin.py
from django.contrib import admin
from .models import ProfilUtilisateur, JournalAction

@admin.register(ProfilUtilisateur)
class ProfilUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'role', 'display_username')
    list_filter = ('role',)
    search_fields = ('utilisateur__username', 'utilisateur__email')
    list_display_links = ('utilisateur', 'role')
    ordering = ('utilisateur__username',)

    def display_username(self, obj):
        return obj.utilisateur.username
    display_username.short_description = 'Nom d’utilisateur'

@admin.register(JournalAction)
class JournalActionAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'action', 'date_action', 'display_username')
    list_filter = ('date_action', 'utilisateur')
    search_fields = ('utilisateur__username', 'action')
    list_display_links = ('action',)
    ordering = ('-date_action',)

    def display_username(self, obj):
        return obj.utilisateur.username
    display_username.short_description = 'Nom d’utilisateur'