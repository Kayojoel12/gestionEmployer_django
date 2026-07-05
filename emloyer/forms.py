

from django import forms
from .models import Employer


class formEmployes(forms.ModelForm):
    class Meta:
        model=Employer
        fields='__all__'
        widgets={
            'nom' :forms.TextInput(attrs={
                'class':'input w-full',
                'placeholder':' Nom'
            }),
            'email' :forms.TextInput(attrs={
                'class':'input w-full',
                'placeholder':'Email'
            }),
            'poste' :forms.TextInput(attrs={
                'class':'input w-full',
                'placeholder':'Poste'
            }),
            'salaire' :forms.TextInput(attrs={
                'class':'input w-full',
                'placeholder':'Salaire'
            }),
        }
