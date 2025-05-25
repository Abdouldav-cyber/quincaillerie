# C:\Users\ASUS\Desktop\ProjetsDjango\quincaillerie\quincaillerie\rapports\models.py
from django.db import models
from django.core.validators import MinValueValidator
from produits.models import Produit
from clients.models import Client

class Stock(models.Model):
    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        related_name='rapport_stocks'
    )
    quantite = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Quantité en stock (doit être positive)"
    )
    seuil_critique = models.IntegerField(
        default=10,
        help_text="Seuil minimum avant alerte de stock faible"
    )
    emplacement = models.CharField(
        max_length=100,
        blank=True,
        default='Entrepôt Principal',
        help_text="Emplacement du stock"
    )
    date_mise_a_jour = models.DateTimeField(
        auto_now=True,
        help_text="Date de la dernière mise à jour du stock"
    )

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite} unités ({self.emplacement})"

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

class Vente(models.Model):
    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        related_name='ventes_rapports'  # Changé pour éviter conflit avec ventes.Vente
    )
    quantite = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Quantité vendue (doit être positive)"
    )
    prix_unitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Prix unitaire de la vente en FCFA"
    )
    date_vente = models.DateTimeField(
        auto_now_add=True,
        help_text="Date et heure de la vente"
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rapports_ventes',  # Ajouté pour résoudre le conflit
        help_text="Client associé à la vente (facultatif)"
    )

    def __str__(self):
        client_info = f" pour {self.client.nom}" if self.client else ""
        return f"Vente de {self.quantite} {self.produit.nom}{client_info} le {self.date_vente.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        verbose_name = "Vente"
        verbose_name_plural = "Ventes"
        ordering = ['-date_vente']

class Depense(models.Model):
    montant = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Montant de la dépense en FCFA"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        help_text="Date et heure de la dépense"
    )
    description = models.TextField(
        blank=True,
        help_text="Description de la dépense (facultatif)"
    )

    def __str__(self):
        return f"Dépense de {self.montant} FCFA le {self.date.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        verbose_name = "Dépense"
        verbose_name_plural = "Dépenses"
        ordering = ['-date']