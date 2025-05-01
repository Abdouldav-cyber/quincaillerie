from django import forms
from .models import CommandeAchat, ArticleAchat

class CommandeAchatForm(forms.ModelForm):
    class Meta:
        model = CommandeAchat
        fields = ['fournisseur', 'date_livraison_prevue', 'statut', 'facture', 'montant_paye']
        widgets = {
            'fournisseur': forms.Select(attrs={'class': 'form-control'}),
            'date_livraison_prevue': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'facture': forms.TextInput(attrs={'class': 'form-control'}),
            'montant_paye': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ArticleAchatForm(forms.ModelForm):
    class Meta:
        model = ArticleAchat
        fields = ['produit', 'quantite', 'prix_unitaire']
        widgets = {
            'produit': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_unitaire': forms.NumberInput(attrs={'class': 'form-control'}),
        }
