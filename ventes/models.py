# C:\Users\ASUS\Desktop\ProjetsDjango\quincaillerie\quincaillerie\ventes\models.py
from django.db import models
from django.core.validators import MinValueValidator  # Pour valider quantite
from django.contrib.auth.models import User
from produits.models import Produit
from clients.models import Client

class Vente(models.Model):
    utilisateur = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ventes',  # Nom unique pour les ventes de l'utilisateur
        help_text="Utilisateur ayant effectué la vente"
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ventes_clients',  # Unique pour éviter conflit avec rapports.Vente
        help_text="Client associé à la vente (facultatif)"
    )
    est_credit = models.BooleanField(
        default=False,
        help_text="Indique si la vente est à crédit"
    )
    tva = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        help_text="Taux de TVA appliqué (en %)"
    )
    montant_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        help_text="Montant total de la vente (calculé automatiquement)"
    )
    date_vente = models.DateTimeField(
        auto_now_add=True,
        help_text="Date et heure de la vente"
    )

    def save(self, *args, **kwargs):
        """Calculer le montant total avant sauvegarde."""
        total = sum(article.prix_unitaire * article.quantite * (1 - article.remise / 100) * (1 + self.tva / 100)
                   for article in self.articles.all())
        self.montant_total = round(total, 2)
        super().save(*args, **kwargs)

    def __str__(self):
        client_info = f" pour {self.client.nom}" if self.client else ""
        return f"Vente {self.id}{client_info} le {self.date_vente.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        verbose_name = "Vente"
        verbose_name_plural = "Ventes"
        ordering = ['-date_vente']

class ArticleVente(models.Model):
    vente = models.ForeignKey(
        Vente,
        on_delete=models.CASCADE,
        related_name='articles',
        help_text="Vente associée à cet article"
    )
    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        help_text="Produit vendu"
    )
    quantite = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Quantité vendue (doit être positive)"
    )
    prix_unitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Prix unitaire du produit en FCFA"
    )
    remise = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        help_text="Remise appliquée en pourcentage (%)"
    )

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom} (Vente {self.vente.id})"

    class Meta:
        verbose_name = "Article de Vente"
        verbose_name_plural = "Articles de Vente"