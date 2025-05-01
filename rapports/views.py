from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ventes.models import Vente
from stocks.models import Stock
from caisse.models import TransactionCaisse
from .forms import FiltreRapportForm
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO
from openpyxl import Workbook
from django.db.models import Sum
from datetime import datetime

@login_required
def rapport_ventes(request):
    form = FiltreRapportForm(request.GET or None)
    ventes = Vente.objects.all()
    total_ventes = 0

    if form.is_valid():
        date_debut = form.cleaned_data.get('date_debut')
        date_fin = form.cleaned_data.get('date_fin')
        if date_debut:
            ventes = ventes.filter(date_vente__gte=date_debut)
        if date_fin:
            ventes = ventes.filter(date_vente__lte=date_fin)

    total_ventes = ventes.aggregate(Sum('montant_total'))['montant_total__sum'] or 0
    return render(request, 'rapports/rapport_ventes.html', {
        'ventes': ventes,
        'total_ventes': total_ventes,
        'form': form
    })

@login_required
def rapport_stocks(request):
    form = FiltreRapportForm(request.GET or None)
    stocks = Stock.objects.all()
    total_valeur = sum(stock.quantite * stock.produit.prix_vente for stock in stocks)
    return render(request, 'rapports/rapport_stocks.html', {
        'stocks': stocks,
        'total_valeur': total_valeur,
        'form': form
    })

@login_required
def rapport_financier(request):
    form = FiltreRapportForm(request.GET or None)
    transactions = TransactionCaisse.objects.all()
    if form.is_valid():
        date_debut = form.cleaned_data.get('date_debut')
        date_fin = form.cleaned_data.get('date_fin')
        if date_debut:
            transactions = transactions.filter(date_creation__gte=date_debut)
        if date_fin:
            transactions = transactions.filter(date_creation__lte=date_fin)

    total_entrees = transactions.filter(type_transaction='entree').aggregate(Sum('montant'))['montant__sum'] or 0
    total_sorties = transactions.filter(type_transaction='sortie').aggregate(Sum('montant'))['montant__sum'] or 0
    solde = total_entrees - total_sorties
    return render(request, 'rapports/rapport_financier.html', {
        'transactions': transactions,
        'total_entrees': total_entrees,
        'total_sorties': total_sorties,
        'solde': solde,
        'form': form
    })

@login_required
def exporter_ventes_csv(request):
    form = FiltreRapportForm(request.GET or None)
    ventes = Vente.objects.all()
    if form.is_valid():
        date_debut = form.cleaned_data.get('date_debut')
        date_fin = form.cleaned_data.get('date_fin')
        if date_debut:
            ventes = ventes.filter(date_vente__gte=date_debut)
        if date_fin:
            ventes = ventes.filter(date_vente__lte=date_fin)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rapport_ventes.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Date', 'Client', 'Montant Total', 'Crédit'])
    for vente in ventes:
        writer.writerow([
            vente.id,
            vente.date_vente,
            vente.client.nom if vente.client else 'Anonyme',
            vente.montant_total,
            vente.est_credit
        ])
    return response

@login_required
def exporter_ventes_pdf(request):
    form = FiltreRapportForm(request.GET or None)
    ventes = Vente.objects.all()
    if form.is_valid():
        date_debut = form.cleaned_data.get('date_debut')
        date_fin = form.cleaned_data.get('date_fin')
        if date_debut:
            ventes = ventes.filter(date_vente__gte=date_debut)
        if date_fin:
            ventes = ventes.filter(date_vente__lte=date_fin)

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.drawString(100, 800, "Rapport des Ventes")
    y = 750
    for vente in ventes:
        p.drawString(50, y, f"ID: {vente.id}, Date: {vente.date_vente}, Client: {vente.client.nom if vente.client else 'Anonyme'}, Montant: {vente.montant_total} FCFA")
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf', headers={'Content-Disposition': 'attachment; filename="rapport_ventes.pdf"'})

@login_required
def exporter_ventes_excel(request):
    form = FiltreRapportForm(request.GET or None)
    ventes = Vente.objects.all()
    if form.is_valid():
        date_debut = form.cleaned_data.get('date_debut')
        date_fin = form.cleaned_data.get('date_fin')
        if date_debut:
            ventes = ventes.filter(date_vente__gte=date_debut)
        if date_fin:
            ventes = ventes.filter(date_vente__lte=date_fin)

    wb = Workbook()
    ws = wb.active
    ws.title = "Rapport des Ventes"
    ws.append(['ID', 'Date', 'Client', 'Montant Total', 'Crédit'])
    for vente in ventes:
        ws.append([
            vente.id,
            vente.date_vente,
            vente.client.nom if vente.client else 'Anonyme',
            vente.montant_total,
            vente.est_credit
        ])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="rapport_ventes.xlsx"'
    wb.save(response)
    return response

@login_required
def exporter_stocks_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rapport_stocks.csv"'
    writer = csv.writer(response)
    writer.writerow(['Produit', 'Quantité', 'Seuil Critique', 'Valeur'])
    for stock in Stock.objects.all():
        writer.writerow([
            stock.produit.nom,
            stock.quantite,
            stock.seuil_critique,
            stock.quantite * stock.produit.prix_vente
        ])
    return response