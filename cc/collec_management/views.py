from django.shortcuts import render

# Create your views here.
def about(request):
    context = {"message" : "Hello, World!"}
    return render(request, 'collec_management/about.html',context)