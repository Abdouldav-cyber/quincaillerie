# C:\Users\ASUS\Desktop\ProjetsDjango\quincaillerie\quincaillerie\rapports\views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Sum, F
import csv
from datetime import datetime
from .models import Stock, Vente, Depense
from .forms import RapportStocksForm, RapportVentesForm, RapportFinancierForm

@login_required
def rapport_stocks(request):
    form = RapportStocksForm(request.GET or None)
    stocks = Stock.objects.all()

    if form.is_valid():
        stocks = form.filter_stocks(stocks)

    total_valeur = stocks.aggregate(
        total=Sum(F('quantite') * F('produit__prix_vente'))
    )['total'] or 0

    return render(request, 'rapports/rapport_stocks.html', {
        'form': form,
        'stocks': stocks,
        'total_valeur': total_valeur,
    })

@login_required
def exporter_stocks_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="rapport_stocks_{datetime.now().strftime("%Y%m%d_%H%M")}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Produit', 'Code-barres', 'Unité', 'Quantité', 'Seuil Critique', 'Emplacement', 'Valeur (FCFA)'])

    stocks = Stock.objects.all()
    form = RapportStocksForm(request.GET or None)
    if form.is_valid():
        stocks = form.filter_stocks(stocks)

    for stock in stocks:
        writer.writerow([
            stock.produit.nom,
            stock.produit.code_barres,
            stock.produit.get_unite_display(),
            stock.quantite,
            stock.seuil_critique,
            stock.emplacement,
            stock.quantite * stock.produit.prix_vente
        ])

    return response

@login_required
def rapport_ventes(request):
    form = RapportVentesForm(request.GET or None)
    ventes = Vente.objects.all()

    if form.is_valid():
        ventes = form.filter_ventes(ventes)

    total_ventes = ventes.aggregate(
        total=Sum(F('quantite') * F('prix_unitaire'))
    )['total'] or 0

    return render(request, 'rapports/rapport_ventes.html', {
        'form': form,
        'ventes': ventes,
        'total_ventes': total_ventes,
    })

@login_required
def exporter_ventes_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="rapport_ventes_{datetime.now().strftime("%Y%m%d_%H%M")}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Produit', 'Code-barres', 'Unité', 'Quantité', 'Prix Unitaire', 'Client', 'Date', 'Total (FCFA)'])

    ventes = Vente.objects.all()
    form = RapportVentesForm(request.GET or None)
    if form.is_valid():
        ventes = form.filter_ventes(ventes)

    for vente in ventes:
        writer.writerow([
            vente.produit.nom,
            vente.produit.code_barres,
            vente.produit.get_unite_display(),
            vente.quantite,
            vente.prix_unitaire,
            vente.client.nom if vente.client else '-',
            vente.date_vente.strftime('%d/%m/%Y %H:%M'),
            vente.quantite * vente.prix_unitaire
        ])

    return response

@login_required
def rapport_financier(request):
    form = RapportFinancierForm(request.GET or None)
    ventes = Vente.objects.all()

    if form.is_valid():
        ventes = form.filter_ventes(ventes)

    total_ventes = ventes.aggregate(
        total=Sum(F('quantite') * F('prix_unitaire'))
    )['total'] or 0

    # Remplacez par un modèle Depense si disponible
    from .models import Depense  # Hypothèse : modèle Depense
    total_depenses = Depense.objects.aggregate(total=Sum('montant'))['total'] or 0
    benefice = total_ventes - total_depenses

    return render(request, 'rapports/rapport_financier.html', {
        'form': form,
        'ventes': ventes,
        'total_ventes': total_ventes,
        'total_depenses': total_depenses,
        'benefice': benefice,
    })

@login_required
def exporter_financier_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="rapport_financier_{datetime.now().strftime("%Y%m%d_%H%M")}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Type', 'Produit', 'Code-barres', 'Unité', 'Quantité', 'Prix Unitaire', 'Client', 'Date', 'Montant (FCFA)'])

    ventes = Vente.objects.all()
    form = RapportFinancierForm(request.GET or None)
    if form.is_valid():
        ventes = form.filter_ventes(ventes)

    for vente in ventes:
        writer.writerow([
            'Vente',
            vente.produit.nom,
            vente.produit.code_barres,
            vente.produit.get_unite_display(),
            vente.quantite,
            vente.prix_unitaire,
            vente.client.nom if vente.client else '-',
            vente.date_vente.strftime('%d/%m/%Y %H:%M'),
            vente.quantite * vente.prix_unitaire
        ])

    # Ajouter les dépenses si le modèle existe
    from .models import Depense  # Hypothèse : modèle Depense
    depenses = Depense.objects.all()
    for depense in depenses:
        writer.writerow([
            'Dépense',
            '-',
            '-',
            '-',
            '-',
            '-',
            '-',
            depense.date.strftime('%d/%m/%Y %H:%M'),
            depense.montant
        ])

    total_ventes = ventes.aggregate(
        total=Sum(F('quantite') * F('prix_unitaire'))
    )['total'] or 0
    total_depenses = Depense.objects.aggregate(total=Sum('montant'))['total'] or 0
    benefice = total_ventes - total_depenses
    writer.writerow(['', '', '', '', '', '', '', 'Total Ventes', total_ventes])
    writer.writerow(['', '', '', '', '', '', '', 'Total Dépenses', total_depenses])
    writer.writerow(['', '', '', '', '', '', '', 'Bénéfice', benefice])

    return response