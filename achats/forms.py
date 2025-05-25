from django import forms
from .models import Achat
from produits.models import Produit

class AchatForm(forms.ModelForm):
    produit = forms.ModelChoiceField(queryset=Produit.objects.all(), empty_label="Sélectionner un produit")

    class Meta:
        model = Achat
        fields = ['produit', 'quantite', 'prix_unitaire', 'fournisseur']
        widgets = {
            'quantite': forms.NumberInput(attrs={'min': 1}),
            'prix_unitaire': forms.NumberInput(attrs={'step': '0.01'}),
            'fournisseur': forms.TextInput(attrs={'placeholder': 'Nom du fournisseur'}),
        }