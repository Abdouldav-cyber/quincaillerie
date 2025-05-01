from django.db import models
from produits.models import Produit

class Stock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='stocks')
    quantite = models.IntegerField()
    seuil_critique = models.IntegerField(default=10)
    emplacement = models.CharField(max_length=100, blank=True, default='Entrepôt Principal')

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite} ({self.emplacement})"

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

class MouvementStock(models.Model):
    TYPE_MOUVEMENT = (
        ('ENTREE', 'Entrée'),
        ('SORTIE', 'Sortie'),
    )
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='mouvements', default=1)
    quantite = models.IntegerField()
    type_mouvement = models.CharField(max_length=10, choices=TYPE_MOUVEMENT)
    date_mouvement = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    raison = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.type_mouvement} de {self.quantite} {self.produit.nom} le {self.date_mouvement}"

    class Meta:
        verbose_name = "Mouvement de Stock"
        verbose_name_plural = "Mouvements de Stock"
        ordering = ['-date_mouvement']
