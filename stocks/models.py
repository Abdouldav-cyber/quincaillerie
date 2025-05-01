from django.db import models
from produits.models import Produit

class Stock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, verbose_name="Produit")
    quantite = models.PositiveIntegerField(verbose_name="Quantité")
    seuil_critique = models.PositiveIntegerField(default=10, verbose_name="Seuil critique")
    emplacement = models.CharField(max_length=100, blank=True, verbose_name="Emplacement")
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite}"

    def est_sous_seuil(self):
        return self.quantite <= self.seuil_critique

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

class MouvementStock(models.Model):
    TYPE_MOUVEMENT = (
        ('entree', 'Entrée'),
        ('sortie', 'Sortie'),
        ('transfert', 'Transfert'),
    )

    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, verbose_name="Stock")
    type_mouvement = models.CharField(max_length=20, choices=TYPE_MOUVEMENT, verbose_name="Type de mouvement")
    quantite = models.PositiveIntegerField(verbose_name="Quantité")
    description = models.TextField(blank=True, verbose_name="Description")
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type_mouvement} - {self.stock.produit.nom}"

    class Meta:
        verbose_name = "Mouvement de Stock"
        verbose_name_plural = "Mouvements de Stock"
