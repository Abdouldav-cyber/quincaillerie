from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Stock, MouvementStock
from .forms import StockForm, MouvementStockForm

@login_required
def liste_mouvements(request):
    mouvements = MouvementStock.objects.all()
    return render(request, 'stocks/liste_mouvements.html', {'mouvements': mouvements})

@login_required
def ajouter_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_mouvements')
    else:
        form = StockForm()
    return render(request, 'stocks/ajouter_stock.html', {'form': form})

@login_required
def ajouter_mouvement(request):
    if request.method == 'POST':
        form = MouvementStockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_mouvements')
    else:
        form = MouvementStockForm()
    return render(request, 'stocks/ajouter_mouvement.html', {'form': form})