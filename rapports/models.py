from django.db import models
from produits.models import Produit

class Stock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='rapport_stocks')
    quantite = models.IntegerField()
    seuil_critique = models.IntegerField(default=10)
    emplacement = models.CharField(max_length=100, blank=True, default='Entrepôt Principal')

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite} ({self.emplacement})"

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='ventes')
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_vente = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Vente de {self.quantite} {self.produit.nom} le {self.date_vente}"

    class Meta:
        verbose_name = "Vente"
        verbose_name_plural = "Ventes"
        ordering = ['-date_vente']