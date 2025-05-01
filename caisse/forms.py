from django import forms
from .models import TransactionCaisse, ClotureCaisse

class TransactionCaisseForm(forms.ModelForm):
    class Meta:
        model = TransactionCaisse
        fields = ['type_transaction', 'montant', 'description']
        widgets = {
            'type_transaction': forms.Select(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class ClotureCaisseForm(forms.ModelForm):
    class Meta:
        model = ClotureCaisse
        fields = ['solde_ouverture', 'solde_cloture', 'notes']
        widgets = {
            'solde_ouverture': forms.NumberInput(attrs={'class': 'form-control'}),
            'solde_cloture': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
