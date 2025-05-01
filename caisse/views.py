from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TransactionCaisse, ClotureCaisse
from .forms import TransactionCaisseForm, ClotureCaisseForm

@login_required
def liste_caisse(request):
    transactions = TransactionCaisse.objects.all()
    clotures = ClotureCaisse.objects.all()
    return render(request, 'caisse/liste_caisse.html', {'transactions': transactions, 'clotures': clotures})

@login_required
def ajouter_transaction_caisse(request):
    if request.method == 'POST':
        form = TransactionCaisseForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.utilisateur = request.user
            transaction.save()
            messages.success(request, 'Transaction enregistrée.')
            return redirect('liste_caisse')
    else:
        form = TransactionCaisseForm()
    return render(request, 'caisse/formulaire_transaction.html', {'form': form, 'titre': 'Nouvelle Transaction'})

@login_required
def ajouter_cloture_caisse(request):
    if request.method == 'POST':
        form = ClotureCaisseForm(request.POST)
        if form.is_valid():
            cloture = form.save(commit=False)
            cloture.utilisateur = request.user
            cloture.save()
            messages.success(request, 'Clôture enregistrée.')
            return redirect('liste_caisse')
    else:
        form = ClotureCaisseForm()
    return render(request, 'caisse/formulaire_cloture.html', {'form': form, 'titre': 'Nouvelle Clôture'})

