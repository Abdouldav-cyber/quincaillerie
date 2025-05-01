from django.db import models
from fournisseurs.models import Fournisseur
from produits.models import Produit

class CommandeAchat(models.Model):
    STATUT_CHOIX = (
        ('en_attente', 'En attente'),
        ('recue', 'Reçue'),
        ('annulee', 'Annulée'),
    )

    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, verbose_name="Fournisseur")
    date_commande = models.DateTimeField(auto_now_add=True, verbose_name="Date de commande")
    date_livraison_prevue = models.DateField(verbose_name="Date de livraison prévue")
    statut = models.CharField(max_length=20, choices=STATUT_CHOIX, default='en_attente', verbose_name="Statut")
    facture = models.CharField(max_length=100, blank=True, verbose_name="Numéro de facture")
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Montant payé")

    def __str__(self):
        return f"Commande {self.id} - {self.fournisseur.nom}"

    class Meta:
        verbose_name = "Commande d'Achat"
        verbose_name_plural = "Commandes d'Achat"

class ArticleAchat(models.Model):
    commande = models.ForeignKey(CommandeAchat, on_delete=models.CASCADE, verbose_name="Commande")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, verbose_name="Produit")
    quantite = models.PositiveIntegerField(verbose_name="Quantité")
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire")

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite}"

    class Meta:
        verbose_name = "Article d'Achat"
        verbose_name_plural = "Articles d'Achat"
