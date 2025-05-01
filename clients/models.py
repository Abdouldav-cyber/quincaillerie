from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=200, verbose_name="Nom")
    email = models.EmailField(blank=True, verbose_name="Email")
    telephone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    adresse = models.TextField(blank=True, verbose_name="Adresse")
    solde = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Solde")
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

class Relance(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
    date_relance = models.DateTimeField(auto_now_add=True, verbose_name="Date de relance")
    message = models.TextField(verbose_name="Message")
    est_automatique = models.BooleanField(default=False, verbose_name="Relance automatique")

    def __str__(self):
        return f"Relance pour {self.client.nom}"

    class Meta:
        verbose_name = "Relance"
        verbose_name_plural = "Relances"
