
from token import NAME

from django.urls import path
from . import views
urlpatterns = [
    path("", views.ListeEmployes,name='liste_employes'),
    path("ajouter", views.AjouterEmloyes,name='ajouter_employes'),
    path("modifier/<int:id>/", views.ModifierEmloyes,name='modifier_employes'),
    path("supprimer/<int:id>/", views.SupprimerEmployer,name='supprimer_employes'),
    

]
