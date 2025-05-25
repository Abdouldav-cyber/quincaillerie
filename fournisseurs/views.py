# C:\Users\ASUS\Desktop\ProjetsDjango\quincaillerie\quincaillerie\fournisseurs\views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Fournisseur
from .forms import FournisseurForm

@login_required
def liste_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'fournisseurs/liste_fournisseurs.html', {'fournisseurs': fournisseurs})

@login_required
def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            fournisseur = form.save()
            messages.success(request, f"Fournisseur {fournisseur.nom} ajouté avec succès.")
            return redirect('fournisseurs:liste_fournisseurs')
    else:
        form = FournisseurForm()
    return render(request, 'fournisseurs/ajouter_fournisseur.html', {'form': form, 'titre': 'Ajouter un Fournisseur'})

@login_required
def modifier_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            fournisseur = form.save()
            messages.success(request, f"Fournisseur {fournisseur.nom} modifié avec succès.")
            return redirect('fournisseurs:liste_fournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'fournisseurs/modifier_fournisseur.html', {'form': form, 'titre': f'Modifier {fournisseur.nom}'})

@login_required
def supprimer_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        fournisseur.delete()
        messages.success(request, f"Fournisseur {fournisseur.nom} supprimé avec succès.")
        return redirect('fournisseurs:liste_fournisseurs')
    return render(request, 'fournisseurs/supprimer_fournisseur.html', {'fournisseur': fournisseur, 'titre': 'Supprimer un Fournisseur'})