from django.db import models
from produits.models import Produit

class CommandeAchat(models.Model):
    fournisseur = models.CharField(max_length=200)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, choices=[('en_attente', 'En attente'), ('livree', 'Livrée'), ('annulee', 'Annulée')], default='en_attente')
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    facture = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Commande {self.id} - {self.fournisseur}"

    class Meta:
        verbose_name = "Commande d'Achat"
        verbose_name_plural = "Commandes d'Achat"
        ordering = ['-date_commande']

class ArticleAchat(models.Model):
    commande = models.ForeignKey(CommandeAchat, on_delete=models.CASCADE, related_name='articles')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom} (Commande {self.commande.id})"

    class Meta:
        verbose_name = "Article d'Achat"
        verbose_name_plural = "Articles d'Achat"

# Conserver le modèle Achat existant
class Achat(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='achats')
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateTimeField(auto_now_add=True)
    fournisseur = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Achat de {self.quantite} {self.produit.nom} le {self.date_achat}"

    class Meta:
        verbose_name = "Achat"
        verbose_name_plural = "Achats"
        ordering = ['-date_achat']