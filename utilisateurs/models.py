# utilisateurs/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class JournalAction(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    action = models.CharField(max_length=255, verbose_name="Action")
    date_action = models.DateTimeField(auto_now_add=True, verbose_name="Date de l'action")

    def __str__(self):
        return f"{self.utilisateur.username} - {self.action} - {self.date_action}"

    class Meta:
        verbose_name = "Journal d'Action"
        verbose_name_plural = "Journaux d'Actions"

class ProfilUtilisateur(models.Model):
    ROLE_CHOIX = (
        ('admin', 'Administrateur'),
        ('vendeur', 'Vendeur'),
        ('magasinier', 'Magasinier'),
        ('comptable', 'Comptable'),
    )

    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    role = models.CharField(max_length=20, choices=ROLE_CHOIX, default='utilisateur', verbose_name="Rôle")

    def __str__(self):
        return f"{self.utilisateur.username} - {self.role}"

    class Meta:
        verbose_name = "Profil Utilisateur"
        verbose_name_plural = "Profils Utilisateur"

@receiver(post_save, sender=User)
def creer_profil_utilisateur(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profilutilisateur'):
        ProfilUtilisateur.objects.create(utilisateur=instance, role='utilisateur')