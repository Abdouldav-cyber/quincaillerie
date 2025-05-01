from django.db import models

class Fournisseur(models.Model):
    nom = models.CharField(max_length=200, verbose_name="Nom")
    email = models.EmailField(blank=True, verbose_name="Email")
    telephone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    adresse = models.TextField(blank=True, verbose_name="Adresse")
    score_fiabilite = models.PositiveIntegerField(default=0, verbose_name="Score de fiabilité")
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Fournisseur"
        verbose_name_plural = "Fournisseurs"
