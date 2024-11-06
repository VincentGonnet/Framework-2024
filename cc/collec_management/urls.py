from django.urls import path
from . import views

urlpatterns = [
    # Page racine, menu principal
    path('', views.index, name='index'),
    # Page d'information à propos de l'application
    path('about/',views.about, name='about'),
    # Page rassemblant toutes les collections
    path('all/',views.liste_collection, name='liste_collection'),
    # Page d'information à propos d'une collection
    path('collection/<int:collection_id>', views.collection, name='collection'),
    # Page de création d'une collection
    path('new/', views.create_collection, name='create_collection'),
    # Page de suppression d'une collection
    path('delete/<int:collection_id>', views.delete_collection, name='delete_collection'),
    # Page de modification d'une collection
    path('change/<int:collection_id>', views.change_collection, name='change_collection')
]