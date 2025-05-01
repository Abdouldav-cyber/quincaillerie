from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Stock, MouvementStock
from .forms import StockForm, MouvementStockForm

@login_required
def liste_stocks(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/liste_stocks.html', {'stocks': stocks})

@login_required
def ajouter_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock ajouté avec succès.')
            return redirect('liste_stocks')
    else:
        form = StockForm()
    return render(request, 'stocks/formulaire_stock.html', {'form': form, 'titre': 'Ajouter un Stock'})

@login_required
def modifier_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock modifié avec succès.')
            return redirect('liste_stocks')
    else:
        form = StockForm(instance=stock)
    return render(request, 'stocks/formulaire_stock.html', {'form': form, 'titre': 'Modifier un Stock'})

@login_required
def ajouter_mouvement_stock(request):
    if request.method == 'POST':
        form = MouvementStockForm(request.POST)
        if form.is_valid():
            mouvement = form.save()
            stock = mouvement.stock
            if mouvement.type_mouvement == 'entree':
                stock.quantite += mouvement.quantite
            elif mouvement.type_mouvement == 'sortie':
                if stock.quantite < mouvement.quantite:
                    messages.error(request, 'Quantité insuffisante en stock.')
                    return redirect('ajouter_mouvement_stock')
                stock.quantite -= mouvement.quantite
            stock.save()
            messages.success(request, 'Mouvement de stock enregistré.')
            return redirect('liste_stocks')
    else:
        form = MouvementStockForm()
    return render(request, 'stocks/formulaire_mouvement.html', {'form': form, 'titre': 'Nouveau Mouvement de Stock'})
