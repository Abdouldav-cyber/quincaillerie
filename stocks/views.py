from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rapports.models import Stock
from .models import MouvementStock
from .forms import StockForm, MouvementStockForm
from utilisateurs.models import JournalAction

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
def liste_stocks(request):
    """
    Affiche la liste de tous les stocks.
    """
    stocks = Stock.objects.all()
    JournalAction.objects.create(
        utilisateur=request.user,
        action="Consultation de la liste des stocks"
    )
    return render(request, 'stocks/liste_stocks.html', {'stocks': stocks})

@login_required
def ajouter_stock(request):
    """
    Permet d'ajouter un nouveau stock.
    """
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save()
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

@login_required
def modifier_stock(request, pk):
    """
    Permet de modifier un stock existant.
    """
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save()
            messages.success(request, f"Stock pour {stock.produit.nom} modifié avec succès.")
            JournalAction.objects.create(
                utilisateur=request.user,
                action=f"Modification du stock pour {stock.produit.nom}"
            )
            return redirect('stocks:liste_stocks')
    else:
        form = StockForm(instance=stock)
    return render(request, 'stocks/modifier_stock.html', {'form': form, 'stock': stock})