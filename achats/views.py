from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AchatForm
from .models import Achat
from rapports.models import Stock
from stocks.models import MouvementStock

@login_required
def liste_achats(request):
    achats = Achat.objects.all()
    return render(request, 'achats/liste_achats.html', {'achats': achats})

@login_required
def ajouter_achat(request):
    if request.method == 'POST':
        form = AchatForm(request.POST)
        if form.is_valid():
            achat = form.save()
            stock, created = Stock.objects.get_or_create(
                produit=achat.produit,
                defaults={'quantite': 0, 'seuil_critique': 10, 'emplacement': 'Entrepôt Principal'}
            )
            stock.quantite += achat.quantite
            stock.save()
            MouvementStock.objects.create(
                produit=achat.produit,
                quantite=achat.quantite,
                type_mouvement='entree',
                description=f"Achat {achat.id}"
            )
            return redirect('liste_achats')
    else:
        form = AchatForm()
    return render(request, 'achats/ajouter_achat.html', {'form': form})

@login_required
def modifier_achat(request, pk):
    achat = Achat.objects.get(pk=pk)
    if request.method == 'POST':
        form = AchatForm(request.POST, instance=achat)
        if form.is_valid():
            ancien_quantite = achat.quantite
            nouveau_achat = form.save()
            # Mettre à jour le stock en fonction de la différence
            stock = Stock.objects.get(produit=achat.produit)
            difference = nouveau_achat.quantite - ancien_quantite
            stock.quantite += difference
            stock.save()
            # Mettre à jour ou créer un mouvement de stock
            MouvementStock.objects.create(
                produit=achat.produit,
                quantite=difference,
                type_mouvement='entree' if difference > 0 else 'ajustement',
                description=f"Modification achat {achat.id}"
            )
            return redirect('liste_achats')
    else:
        form = AchatForm(instance=achat)
    return render(request, 'achats/modifier_achat.html', {'form': form, 'achat': achat})