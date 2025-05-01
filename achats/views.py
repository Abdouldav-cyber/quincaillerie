from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CommandeAchat, ArticleAchat
from .forms import CommandeAchatForm, ArticleAchatForm
from stocks.models import Stock, MouvementStock

from django.forms import inlineformset_factory
from .forms import ArticleAchatForm

@login_required
def ajouter_article_achat(request, commande_pk):
    commande = get_object_or_404(CommandeAchat, pk=commande_pk)
    ArticleAchatFormSet = inlineformset_factory(CommandeAchat, ArticleAchat, form=ArticleAchatForm, extra=1)
    
    if request.method == 'POST':
        formset = ArticleAchatFormSet(request.POST, instance=commande)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Articles ajoutés avec succès.')
            return redirect('liste_achats')
    else:
        formset = ArticleAchatFormSet(instance=commande)
    
    return render(request, 'achats/formulaire_article_achat.html', {
        'formset': formset,
        'commande': commande,
        'titre': f'Ajouter des Articles à la Commande {commande.id}'
    })

@login_required
def liste_achats(request):
    commandes = CommandeAchat.objects.all()
    return render(request, 'achats/liste_achats.html', {'commandes': commandes})

@login_required
def ajouter_achat(request):
    if request.method == 'POST':
        form = CommandeAchatForm(request.POST)
        if form.is_valid():
            commande = form.save()
            messages.success(request, 'Commande ajoutée avec succès.')
            return redirect('liste_achats')
    else:
        form = CommandeAchatForm()
    return render(request, 'achats/formulaire_achat.html', {'form': form, 'titre': 'Ajouter une Commande'})

@login_required
def modifier_achat(request, pk):
    commande = get_object_or_404(CommandeAchat, pk=pk)
    if request.method == 'POST':
        form = CommandeAchatForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            if form.cleaned_data['statut'] == 'recue':
                for article in commande.articleachat_set.all():
                    stock, created = Stock.objects.get_or_create(produit=article.produit, defaults={'quantite': 0})
                    stock.quantite += article.quantite
                    stock.save()
                    MouvementStock.objects.create(
                        stock=stock,
                        type_mouvement='entree',
                        quantite=article.quantite,
                        description=f"Réception commande {commande.id}"
                    )
            messages.success(request, 'Commande modifiée avec succès.')
            return redirect('liste_achats')
    else:
        form = CommandeAchatForm(instance=commande)
    return render(request, 'achats/formulaire_achat.html', {'form': form, 'titre': 'Modifier une Commande'})
