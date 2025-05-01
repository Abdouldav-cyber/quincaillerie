from django import forms
from .models import Produit, Categorie

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'categorie', 'unite', 'prix_achat', 'prix_vente', 'prix_gros', 'remise', 'reference_fournisseur', 'code_barres']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'unite': forms.Select(attrs={'class': 'form-control'}),
            'prix_achat': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_vente': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_gros': forms.NumberInput(attrs={'class': 'form-control'}),
            'remise': forms.NumberInput(attrs={'class': 'form-control'}),
            'reference_fournisseur': forms.TextInput(attrs={'class': 'form-control'}),
            'code_barres': forms.TextInput(attrs={'class': 'form-control'}),
        }
