from django.db import models
from django.contrib.auth.models import User

class TransactionCaisse(models.Model):
    TYPE_TRANSACTION = (
        ('entree', 'Entrée'),
        ('sortie', 'Sortie'),
    )

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    type_transaction = models.CharField(max_length=10, choices=TYPE_TRANSACTION, verbose_name="Type de transaction")
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant")
    description = models.TextField(blank=True, verbose_name="Description")
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type_transaction} - {self.montant}"

    class Meta:
        verbose_name = "Transaction de Caisse"
        verbose_name_plural = "Transactions de Caisse"

class ClotureCaisse(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    date_cloture = models.DateTimeField(auto_now_add=True, verbose_name="Date de clôture")
    solde_ouverture = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Solde d'ouverture")
    solde_cloture = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Solde de clôture")
    notes = models.TextField(blank=True, verbose_name="Notes")

    def __str__(self):
        return f"Clôture {self.id} - {self.date_cloture}"

    class Meta:
        verbose_name = "Clôture de Caisse"
        verbose_name_plural = "Clôtures de Caisse"
