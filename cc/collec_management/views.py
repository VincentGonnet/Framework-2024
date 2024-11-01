from django.shortcuts import render
from django.http import Http404
from .models import Collec

# Create your views here.
def about(request):
    context = {"message" : "Hello, World!"}
    return render(request, 'collec_management/about.html',context)

def collection(request,collection_id):
    try:
        context = Collec.objects.get(pk=collection_id)
    except Collec.DoesNotExist:
        raise Http404("Collection does not exist")
    return render(request, 'collec_management/collection.html',{'context':context})
