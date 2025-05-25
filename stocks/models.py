from django.db import models
from produits.models import Produit

class MouvementStock(models.Model):
    TYPE_MOUVEMENT = (
        ('entree', 'Entrée'),
        ('sortie', 'Sortie'),
        ('ajustement', 'Ajustement'),
    )
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='mouvements')
    quantite = models.IntegerField()
    type_mouvement = models.CharField(max_length=20, choices=TYPE_MOUVEMENT)
    date_mouvement = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.type_mouvement} de {self.quantite} {self.produit.nom}"

    class Meta:
        verbose_name = "Mouvement de Stock"
        verbose_name_plural = "Mouvements de Stock"
        ordering = ['-date_mouvement']