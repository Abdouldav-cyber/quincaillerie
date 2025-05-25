from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rapports.models import Stock
from .models import MouvementStock
from .forms import StockForm, MouvementStockForm
from utilisateurs.models import JournalAction  # Ajout pour la journalisation

@login_required
def liste_mouvements(request):
    """
    Affiche la liste de tous les mouvements de stock.
    """
    mouvements = MouvementStock.objects.all()
    JournalAction.objects.create(
        utilisateur=request.user,
        action="Consultation de la liste des mouvements de stock"
    )
    return render(request, 'stocks/liste_mouvements.html', {'mouvements': mouvements})

@login_required
def ajouter_stock(request):
    """
    Permet d'ajouter un nouveau stock.
    """
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save()  # Utilisation de form.save() pour plus de simplicité
            messages.success(request, f"Stock pour {stock.produit.nom} ajouté avec succès.")
            JournalAction.objects.create(
                utilisateur=request.user,
                action=f"Ajout d'un stock pour {stock.produit.nom}"
            )
            return redirect('stocks:liste_mouvements')
    else:
        form = StockForm()
    return render(request, 'stocks/ajouter_stock.html', {'form': form})

@login_required
def ajouter_mouvement(request):
    """
    Permet d'ajouter un nouveau mouvement de stock.
    """
    if request.method == 'POST':
        form = MouvementStockForm(request.POST)
        if form.is_valid():
            mouvement = form.save()
            messages.success(request, f"Mouvement de stock ({mouvement.type_mouvement}) pour {mouvement.produit.nom} ajouté avec succès.")
            JournalAction.objects.create(
                utilisateur=request.user,
                action=f"Ajout d'un mouvement de stock ({mouvement.type_mouvement}) pour {mouvement.produit.nom}"
            )
            return redirect('stocks:liste_mouvements')
    else:
        form = MouvementStockForm()
    return render(request, 'stocks/ajouter_mouvement.html', {'form': form})