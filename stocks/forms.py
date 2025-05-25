from django import forms
from .models import MouvementStock
from produits.models import Produit

class StockForm(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.all(), label="Produit")
    quantite = forms.IntegerField(min_value=0, label="Quantité")
    seuil_critique = forms.IntegerField(min_value=0, required=False, label="Seuil Critique")
    emplacement = forms.CharField(max_length=100, required=False, label="Emplacement")

class MouvementStockForm(forms.ModelForm):
    class Meta:
        model = MouvementStock
        fields = ['produit', 'quantite', 'type_mouvement', 'description']
        widgets = {
            'produit': forms.Select(),
            'quantite': forms.NumberInput(attrs={'min': 1}),
            'type_mouvement': forms.Select(),
            'description': forms.Textarea(attrs={'rows': 4}),
        }