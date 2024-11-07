from django.shortcuts import render, redirect
from django.http import Http404
from .models import Collec
from .forms import CreateCollectionForm, ChangeCollectionForm

# Page racine, menu principal
def index(request):
    return render(request, 'index.html')

# Page d'information à propos de l'application
def about(request):
    return render(request, 'collec_management/about.html')

# Page d'information à propos d'une collection
def collection(request, collection_id):
    try:
        context = Collec.objects.get(pk=collection_id)
    except Collec.DoesNotExist:
        raise Http404("Collection does not exist")
    created = request.GET.get('created', 'False') == 'True'  # Permet de savoir si la collection vient d'être créée
    edited = request.GET.get('edited', 'False') == 'True'  # Permet de savoir si la collection vient d'être modifiée
    return render(request, 'collec_management/collection.html', {'context': context,
                                                                 'created': created,
                                                                 'edited': edited})

# Page rassemblant toutes les collections
def liste_collection(request):
    collections = Collec.objects.all()
    return render(request,'collec_management/collec_liste.html', {'collections': collections})

# Page de création d'une collection
def create_collection(request):
    if request.method == 'POST':
        form = CreateCollectionForm(request.POST)
        if form.is_valid():
            new_collection = form.save()
            # Redirection vers la page de la collection nouvellement créée avec un message de confirmation
            return redirect(f'/collection/{new_collection.id}?created=True')
    else:
        form = CreateCollectionForm()
    return render(request,'collec_management/create_collection.html', {'form': form})

# Page de suppression d'une collection
def delete_collection(request, collection_id):
    try:
        collection = Collec.objects.get(pk=collection_id)
    except Collec.DoesNotExist:
        raise Http404("Collection does not exist")
    
    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')
        if confirmation == 'delete':
            collection.delete()
        return redirect('liste_collection')
    
    return render(request, 'collec_management/delete_collection.html', {'context': collection})

# Page de modification d'une collection
def change_collection(request, collection_id):
    try:
        collection = Collec.objects.get(pk=collection_id)
    except Collec.DoesNotExist:
        raise Http404("Collection does not exist")
    
    if request.method == 'POST':
        form = ChangeCollectionForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect(f'/collection/{collection.id}?edited=True')
    else:
        form = ChangeCollectionForm(instance=collection)
    return render(request, 'collec_management/change_collection.html', {'form': form, 'collection': collection})
