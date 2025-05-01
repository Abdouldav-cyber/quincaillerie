from django import forms
from .models import Stock, MouvementStock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['produit', 'quantite', 'seuil_critique', 'emplacement']
        widgets = {
            'produit': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'seuil_critique': forms.NumberInput(attrs={'class': 'form-control'}),
            'emplacement': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MouvementStockForm(forms.ModelForm):
    class Meta:
        model = MouvementStock
        fields = ['produit', 'quantite', 'type_mouvement', 'description', 'raison']
        widgets = {
            'produit': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'type_mouvement': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'raison': forms.TextInput(attrs={'class': 'form-control'}),
        }