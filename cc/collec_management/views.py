from django.shortcuts import render, redirect
from django.http import Http404
from .models import Collec

# Page d'information à propos de l'application
def about(request):
    return render(request, 'collec_management/about.html')

# Page d'information à propos d'une collection
def collection(request, collection_id):
    try:
        context = Collec.objects.get(pk=collection_id)
    except Collec.DoesNotExist:
        raise Http404("Collection does not exist")
    return render(request, 'collec_management/collection.html', {'context': context})

# Page rassemblant toutes les collections
def liste_collection(request):
    collections = Collec.objects.all()
    return render(request,'collec_management/collec_liste.html', {'collections': collections})

# Page de création d'une collection
def create_collection(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        new_collection = Collec.objects.create(name=name,
                                               description=description)
        return collection(request, new_collection.id)
    return render(request,'collec_management/create_collection.html')

# Page de suppression d'une collection
def delete_collection(request, collection_id):
    try:
        collection = Collec.objects.get(pk=collection_id)
    except Collec.DoesNotExist:
        raise Http404("Collection does not exist")
    
    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')
        if confirmation == 'yes':
            collection.delete()

        return redirect('liste_collection')
    
    return render(request, 'collec_management/delete_collection.html', {'context': collection})