# Module rassemblant les formulaires de l'application
from django import forms
from .models import Collec

# Formulaire de création d'une collection
class CreateCollectionForm(forms.ModelForm):
    class Meta:
        model = Collec
        fields = ['name', 'description']
        labels = {
            'name': 'Nom de la collection',
            'description': 'Description de la collection',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'minlength': '5',
                'maxlength': '100',
                'required': 'required',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
        }

# Formulaire de modification d'une collection
class ChangeCollectionForm(forms.ModelForm):
    class Meta:
        model = Collec
        fields = ['name', 'description']
        labels = {
            'name': 'Nom de la collection',
            'description': 'Description de la collection',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'minlength': '5',
                'maxlength': '100',
                'required': 'required'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
        }
