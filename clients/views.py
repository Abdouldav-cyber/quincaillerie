# C:\Users\ASUS\Desktop\ProjetsDjango\quincaillerie\quincaillerie\clients\views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Client, Relance
from .forms import ClientForm, RelanceForm

@login_required
def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/liste_clients.html', {'clients': clients})

@login_required
def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client ajouté avec succès.')
            return redirect('clients:liste_clients')
    else:
        form = ClientForm()
    return render(request, 'clients/formulaire_client.html', {'form': form, 'titre': 'Ajouter un Client'})

@login_required
def modifier_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client modifié avec succès.')
            return redirect('clients:liste_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/formulaire_client.html', {'form': form, 'titre': f'Modifier {client.nom}'})

@login_required
def ajouter_relance(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk)
    if request.method == 'POST':
        form = RelanceForm(request.POST)
        if form.is_valid():
            relance = form.save(commit=False)
            relance.client = client
            relance.save()
            messages.success(request, 'Relance enregistrée.')
            return redirect('clients:liste_clients')
    else:
        form = RelanceForm()
    return render(request, 'clients/formulaire_client.html', {'form': form, 'titre': f'Relance pour {client.nom}'})

@login_required
def supprimer_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, f"Client {client.nom} supprimé avec succès.")
        return redirect('clients:liste_clients')
    return render(request, 'clients/supprimer_client.html', {'client': client, 'titre': f'Supprimer {client.nom}'})