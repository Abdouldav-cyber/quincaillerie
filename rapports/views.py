from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Sum, F
import csv
from .models import Stock, Vente
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
    response['Content-Disposition'] = 'attachment; filename="rapport_stocks.csv"'

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
    response['Content-Disposition'] = 'attachment; filename="rapport_ventes.csv"'

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
            vente.client or '-',
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
    total_depenses = 0  # À remplacer si un modèle Depense existe
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
    response['Content-Disposition'] = 'attachment; filename="rapport_financier.csv"'

    writer = csv.writer(response)
    writer.writerow(['Produit', 'Code-barres', 'Unité', 'Quantité', 'Prix Unitaire', 'Client', 'Date', 'Total Vente (FCFA)'])

    ventes = Vente.objects.all()
    form = RapportFinancierForm(request.GET or None)
    if form.is_valid():
        ventes = form.filter_ventes(ventes)

    for vente in ventes:
        writer.writerow([
            vente.produit.nom,
            vente.produit.code_barres,
            vente.produit.get_unite_display(),
            vente.quantite,
            vente.prix_unitaire,
            vente.client or '-',
            vente.date_vente.strftime('%d/%m/%Y %H:%M'),
            vente.quantite * vente.prix_unitaire
        ])

    total_ventes = ventes.aggregate(
        total=Sum(F('quantite') * F('prix_unitaire'))
    )['total'] or 0
    total_depenses = 0  # À remplacer si un modèle Depense existe
    benefice = total_ventes - total_depenses
    writer.writerow(['', '', '', '', '', '', 'Total Ventes', total_ventes])
    writer.writerow(['', '', '', '', '', '', 'Total Dépenses', total_depenses])
    writer.writerow(['', '', '', '', '', '', 'Bénéfice', benefice])

    return response