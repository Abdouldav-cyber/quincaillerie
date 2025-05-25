from django.db import models
from django.contrib.auth.models import User
from produits.models import Produit
from clients.models import Client

class Vente(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    est_credit = models.BooleanField(default=False)
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_vente = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vente pour {self.client} le {self.date_vente}"

    class Meta:
        verbose_name = "Vente"
        verbose_name_plural = "Ventes"
        ordering = ['-date_vente']

class ArticleVente(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name='articles')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    remise = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom} (Vente {self.vente.id})"

    class Meta:
        verbose_name = "Article de Vente"
        verbose_name_plural = "Articles de Vente"