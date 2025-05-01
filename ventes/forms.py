from django import forms
from .models import Vente, ArticleVente

class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['client', 'est_credit', 'tva']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'est_credit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tva': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ArticleVenteForm(forms.ModelForm):
    class Meta:
        model = ArticleVente
        fields = ['produit', 'quantite', 'prix_unitaire', 'remise']
        widgets = {
            'produit': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_unitaire': forms.NumberInput(attrs={'class': 'form-control'}),
            'remise': forms.NumberInput(attrs={'class': 'form-control'}),
        }
