from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import formset_factory
from .models import Vente, ArticleVente
from .forms import VenteForm, ArticleVenteForm
from stocks.models import Stock, MouvementStock
from utilisateurs.models import JournalAction

@login_required
def liste_ventes(request):
    """
    Affiche la liste de toutes les ventes.
    """
    ventes = Vente.objects.all()
    JournalAction.objects.create(
        utilisateur=request.user,
        action="Consultation de la liste des ventes"
    )
    return render(request, 'ventes/liste_ventes.html', {'ventes': ventes})

@login_required
def ajouter_vente(request):
    """
    Permet d'ajouter une nouvelle vente avec plusieurs articles.
    Met à jour le stock et enregistre un mouvement de stock pour chaque article.
    """
    ArticleVenteFormSet = formset_factory(ArticleVenteForm, extra=1)
    
    if request.method == 'POST':
        vente_form = VenteForm(request.POST)
        formset = ArticleVenteFormSet(request.POST)
        
        if vente_form.is_valid() and formset.is_valid():
            # Créer la vente
            vente = vente_form.save(commit=False)
            vente.utilisateur = request.user
            vente.montant_total = 0
            vente.save()
            
            # Traiter chaque article
            for form in formset:
                article = form.save(commit=False)
                article.vente = vente
                # Vérifier le stock
                stock = get_object_or_404(Stock, produit=article.produit)
                if stock.quantite < article.quantite:
                    messages.error(request, f"Stock insuffisant pour {article.produit.nom}.")
                    vente.delete()
                    return redirect('ajouter_vente')
                
                # Enregistrer l'article
                article.save()
                
                # Mettre à jour le stock
                stock.quantite -= article.quantite
                stock.save()
                
                # Enregistrer le mouvement de stock
                MouvementStock.objects.create(
                    stock=stock,
                    type_mouvement='sortie',
                    quantite=article.quantite,
                    description=f"Vente {vente.id}"
                )
                
                # Calculer le montant total
                article_total = (article.prix_unitaire * article.quantite) * (1 - article.remise / 100)
                vente.montant_total += article_total
            
            # Appliquer la TVA
            vente.montant_total *= (1 + vente.tva / 100)
            vente.save()
            
            # Mettre à jour le solde du client si vente à crédit
            if vente.client and vente.est_credit:
                vente.client.solde += vente.montant_total
                vente.client.save()
            
            # Journalisation
            JournalAction.objects.create(
                utilisateur=request.user,
                action=f"Ajout de la vente {vente.id}"
            )
            
            messages.success(request, 'Vente enregistrée avec succès.')
            return redirect('liste_ventes')
    else:
        vente_form = VenteForm()
        formset = ArticleVenteFormSet()
    
    return render(request, 'ventes/formulaire_vente.html', {
        'vente_form': vente_form,
        'formset': formset,
        'titre': 'Nouvelle Vente'
    })

@login_required
def voir_ticket_vente(request, pk):
    """
    Affiche le ticket détaillé d'une vente spécifique.
    """
    vente = get_object_or_404(Vente, pk=pk)
    JournalAction.objects.create(
        utilisateur=request.user,
        action=f"Consultation du ticket de vente {vente.id}"
    )
    return render(request, 'ventes/ticket_vente.html', {'vente': vente})