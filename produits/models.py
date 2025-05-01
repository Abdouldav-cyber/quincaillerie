from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

class Produit(models.Model):
    UNITE_CHOIX = (
        ('piece', 'Pièce'),
        ('boite', 'Boîte'),
        ('kg', 'Kilogramme'),
        ('litre', 'Litre'),
    )

    nom = models.CharField(max_length=200)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name="Catégorie")
    unite = models.CharField(max_length=20, choices=UNITE_CHOIX, verbose_name="Unité")
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix d'achat")
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix de vente")
    prix_gros = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Prix de gros")
    remise = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name="Remise")
    reference_fournisseur = models.CharField(max_length=100, blank=True, verbose_name="Référence fournisseur")
    code_barres = models.CharField(max_length=50, unique=True, blank=True, verbose_name="Code-barres")
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"