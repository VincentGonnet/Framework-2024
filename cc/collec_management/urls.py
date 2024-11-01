from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about, name='about'),
    path('collection/<int:collection_id>', views.collection, name='collection'),
    path('all/',views.liste_collection, name='liste_collection')
]