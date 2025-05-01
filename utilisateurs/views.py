from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import ProfilUtilisateur
from .forms import UtilisateurForm, ProfilUtilisateurForm

@login_required
def liste_utilisateurs(request):
    if request.user.profilutilisateur.role != 'admin':
        messages.error(request, "Accès réservé aux administrateurs.")
        return redirect('accueil')
    utilisateurs = User.objects.all()
    return render(request, 'utilisateurs/liste_utilisateurs.html', {'utilisateurs': utilisateurs})

@login_required
def ajouter_utilisateur(request):
    if request.user.profilutilisateur.role != 'admin':
        messages.error(request, "Accès réservé aux administrateurs.")
        return redirect('accueil')
    if request.method == 'POST':
        utilisateur_form = UtilisateurForm(request.POST)
        profil_form = ProfilUtilisateurForm(request.POST)
        if utilisateur_form.is_valid() and profil_form.is_valid():
            utilisateur = utilisateur_form.save(commit=False)
            utilisateur.set_password(utilisateur_form.cleaned_data['password'])
            utilisateur.save()
            profil = profil_form.save(commit=False)
            profil.utilisateur = utilisateur
            profil.save()
            messages.success(request, 'Utilisateur ajouté avec succès.')
            return redirect('liste_utilisateurs')
    else:
        utilisateur_form = UtilisateurForm()
        profil_form = ProfilUtilisateurForm()
    return render(request, 'utilisateurs/formulaire_utilisateur.html', {
        'utilisateur_form': utilisateur_form,
        'profil_form': profil_form,
        'titre': 'Ajouter un Utilisateur'
    })

@login_required
def modifier_utilisateur(request, pk):
    if request.user.profilutilisateur.role != 'admin':
        messages.error(request, "Accès réservé aux administrateurs.")
        return redirect('accueil')
    utilisateur = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        utilisateur_form = UtilisateurForm(request.POST, instance=utilisateur)
        profil_form = ProfilUtilisateurForm(request.POST, instance=utilisateur.profilutilisateur)
        if utilisateur_form.is_valid() and profil_form.is_valid():
            utilisateur = utilisateur_form.save()
            if utilisateur_form.cleaned_data['password']:
                utilisateur.set_password(utilisateur_form.cleaned_data['password'])
                utilisateur.save()
            profil_form.save()
            messages.success(request, 'Utilisateur modifié avec succès.')
            return redirect('liste_utilisateurs')
    else:
        utilisateur_form = UtilisateurForm(instance=utilisateur)
        profil_form = ProfilUtilisateurForm(instance=utilisateur.profilutilisateur)
    return render(request, 'utilisateurs/formulaire_utilisateur.html', {
        'utilisateur_form': utilisateur_form,
        'profil_form': profil_form,
        'titre': 'Modifier un Utilisateur'
    })