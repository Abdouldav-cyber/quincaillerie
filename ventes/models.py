from django.db import models
from produits.models import Produit
from clients.models import Client

class Vente(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Client")
    date_vente = models.DateTimeField(auto_now_add=True, verbose_name="Date de vente")
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant total")
    est_credit = models.BooleanField(default=False, verbose_name="Vente à crédit")
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name="TVA")
    utilisateur = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Utilisateur")

    def __str__(self):
        return f"Vente {self.id} - {self.date_vente}"

    class Meta:
        verbose_name = "Vente"
        verbose_name_plural = "Ventes"

class ArticleVente(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, verbose_name="Vente")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, verbose_name="Produit")
    quantite = models.PositiveIntegerField(verbose_name="Quantité")
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire")
    remise = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name="Remise")

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite}"

    class Meta:
        verbose_name = "Article de Vente"
        verbose_name_plural = "Articles de Vente"
