# C:\Users\ASUS\Desktop\ProjetsDjango\quincaillerie\quincaillerie\rapports\forms.py
from django import forms
from django.db.models import Q
from produits.models import Produit, Categorie
from rapports.models import Stock, Vente

class RapportStocksForm(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.all(), required=False, label="Produit")
    code_barres = forms.CharField(max_length=50, required=False, label="Code-barres")
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all(), required=False, label="Catégorie")
    emplacement = forms.CharField(max_length=100, required=False, label="Emplacement")
    seuil_critique = forms.IntegerField(required=False, label="Seuil Critique")

    def filter_stocks(self, queryset):
        if self.is_valid():
            produit = self.cleaned_data.get('produit')
            code_barres = self.cleaned_data.get('code_barres')
            categorie = self.cleaned_data.get('categorie')
            emplacement = self.cleaned_data.get('emplacement')
            seuil_critique = self.cleaned_data.get('seuil_critique')

            if produit:
                queryset = queryset.filter(produit=produit)
            if code_barres:
                queryset = queryset.filter(produit__code_barres__icontains=code_barres)
            if categorie:
                queryset = queryset.filter(produit__categorie=categorie)
            if emplacement:
                queryset = queryset.filter(emplacement__icontains=emplacement)
            if seuil_critique is not None:
                queryset = queryset.filter(seuil_critique__lte=seuil_critique)

        return queryset

class RapportVentesForm(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.all(), required=False, label="Produit")
    code_barres = forms.CharField(max_length=50, required=False, label="Code-barres")
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all(), required=False, label="Catégorie")
    date_debut = forms.DateField(required=False, label="Date de début", widget=forms.DateInput(attrs={'type': 'date'}))
    date_fin = forms.DateField(required=False, label="Date de fin", widget=forms.DateInput(attrs={'type': 'date'}))
    client = forms.CharField(max_length=200, required=False, label="Client")

    def filter_ventes(self, queryset):
        if self.is_valid():
            produit = self.cleaned_data.get('produit')
            code_barres = self.cleaned_data.get('code_barres')
            categorie = self.cleaned_data.get('categorie')
            date_debut = self.cleaned_data.get('date_debut')
            date_fin = self.cleaned_data.get('date_fin')
            client = self.cleaned_data.get('client')

            if produit:
                queryset = queryset.filter(produit=produit)
            if code_barres:
                queryset = queryset.filter(produit__code_barres__icontains=code_barres)
            if categorie:
                queryset = queryset.filter(produit__categorie=categorie)
            if date_debut:
                queryset = queryset.filter(date_vente__gte=date_debut)
            if date_fin:
                queryset = queryset.filter(date_vente__lte=date_fin)
            if client:
                queryset = queryset.filter(client__nom__icontains=client)  # Correction ici

        return queryset

class RapportFinancierForm(RapportVentesForm):
    pass