from django import forms
from django.db.models import F
from produits.models import Categorie

class FiltreRapportForm(forms.Form):
    date_debut = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Date de début'
    )
    date_fin = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Date de fin'
    )

class RapportStocksForm(forms.Form):
    produit = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du produit'}),
        label='Produit'
    )
    code_barres = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code-barres'}),
        label='Code-barres'
    )
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Catégorie'
    )
    seuil_critique = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='Seuil critique atteint'
    )
    emplacement = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emplacement'}),
        label='Emplacement'
    )

    def filter_stocks(self, queryset):
        if self.cleaned_data['produit']:
            queryset = queryset.filter(produit__nom__icontains=self.cleaned_data['produit'])
        if self.cleaned_data['code_barres']:
            queryset = queryset.filter(produit__code_barres__icontains=self.cleaned_data['code_barres'])
        if self.cleaned_data['categorie']:
            queryset = queryset.filter(produit__categorie=self.cleaned_data['categorie'])
        if self.cleaned_data['seuil_critique']:
            queryset = queryset.filter(quantite__lte=F('seuil_critique'))
        if self.cleaned_data['emplacement']:
            queryset = queryset.filter(emplacement__icontains=self.cleaned_data['emplacement'])
        return queryset

class RapportVentesForm(forms.Form):
    produit = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du produit'}),
        label='Produit'
    )
    code_barres = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code-barres'}),
        label='Code-barres'
    )
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Catégorie'
    )
    date_debut = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Date de début'
    )
    date_fin = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Date de fin'
    )
    client = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du client'}),
        label='Client'
    )

    def filter_ventes(self, queryset):
        if self.cleaned_data['produit']:
            queryset = queryset.filter(produit__nom__icontains=self.cleaned_data['produit'])
        if self.cleaned_data['code_barres']:
            queryset = queryset.filter(produit__code_barres__icontains=self.cleaned_data['code_barres'])
        if self.cleaned_data['categorie']:
            queryset = queryset.filter(produit__categorie=self.cleaned_data['categorie'])
        if self.cleaned_data['date_debut']:
            queryset = queryset.filter(date_vente__gte=self.cleaned_data['date_debut'])
        if self.cleaned_data['date_fin']:
            queryset = queryset.filter(date_vente__lte=self.cleaned_data['date_fin'])
        if self.cleaned_data['client']:
            queryset = queryset.filter(client__icontains=self.cleaned_data['client'])
        return queryset

class RapportFinancierForm(forms.Form):
    produit = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du produit'}),
        label='Produit'
    )
    code_barres = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code-barres'}),
        label='Code-barres'
    )
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Catégorie'
    )
    date_debut = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Date de début'
    )
    date_fin = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Date de fin'
    )
    client = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du client'}),
        label='Client'
    )

    def filter_ventes(self, queryset):
        if self.cleaned_data['produit']:
            queryset = queryset.filter(produit__nom__icontains=self.cleaned_data['produit'])
        if self.cleaned_data['code_barres']:
            queryset = queryset.filter(produit__code_barres__icontains=self.cleaned_data['code_barres'])
        if self.cleaned_data['categorie']:
            queryset = queryset.filter(produit__categorie=self.cleaned_data['categorie'])
        if self.cleaned_data['date_debut']:
            queryset = queryset.filter(date_vente__gte=self.cleaned_data['date_debut'])
        if self.cleaned_data['date_fin']:
            queryset = queryset.filter(date_vente__lte=self.cleaned_data['date_fin'])
        if self.cleaned_data['client']:
            queryset = queryset.filter(client__icontains=self.cleaned_data['client'])
        return queryset