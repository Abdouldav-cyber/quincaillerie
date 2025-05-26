# C:\Users\ASUS\Desktop\ProjetsDjango\quincaillerie\quincaillerie\achats\views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            try:
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
                messages.success(request, "Achat ajouté avec succès.")
                return redirect('achats:liste_achats')  # Ajouté le namespace 'achats:'
            except Exception as e:
                messages.error(request, f"Erreur lors de l'ajout de l'achat : {str(e)}")
    else:
        form = AchatForm()
    return render(request, 'achats/ajouter_achat.html', {'form': form})

@login_required
def modifier_achat(request, pk):
    achat = get_object_or_404(Achat, pk=pk)  # Utilisé get_object_or_404 pour gérer les erreurs 404
    if request.method == 'POST':
        form = AchatForm(request.POST, instance=achat)
        if form.is_valid():
            try:
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
                messages.success(request, "Achat modifié avec succès.")
                return redirect('achats:liste_achats')  # Ajouté le namespace 'achats:'
            except Stock.DoesNotExist:
                messages.error(request, "Erreur : Le stock pour ce produit n'existe pas.")
            except Exception as e:
                messages.error(request, f"Erreur lors de la modification de l'achat : {str(e)}")
    else:
        form = AchatForm(instance=achat)
    return render(request, 'achats/modifier_achat.html', {'form': form, 'achat': achat})