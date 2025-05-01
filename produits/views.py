from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Produit, Categorie
from .forms import ProduitForm
from utilisateurs.models import JournalAction

@login_required
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits/liste_produits.html', {'produits': produits})

@login_required
def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit ajouté avec succès.')
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'produits/formulaire_produit.html', {'form': form, 'titre': 'Ajouter un Produit'})

@login_required
def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit modifié avec succès.')
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'produits/formulaire_produit.html', {'form': form, 'titre': 'Modifier un Produit'})

@login_required
def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        messages.success(request, 'Produit supprimé avec succès.')
        return redirect('liste_produits')
    return render(request, 'produits/formulaire_produit.html', {'produit': produit, 'titre': 'Supprimer un Produit'})
@login_required
def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            produit = form.save()
            JournalAction.objects.create(
                utilisateur=request.user,
                action=f"Ajout du produit {produit.nom}"
            )
            messages.success(request, 'Produit ajouté avec succès.')
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'produits/formulaire_produit.html', {'form': form, 'titre': 'Ajouter un Produit'})