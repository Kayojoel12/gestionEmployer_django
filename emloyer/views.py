from os import name

from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from emloyer.models import Employer
from .forms import formEmployes
# Create your views here.

def ListeEmployes(request):
    employes=Employer.objects.all()
    return render(request,'employes/liste.html',{'employes':employes})

def AjouterEmloyes(request):
    form= formEmployes(request.POST or None)
    if form.is_valid() :
        form.save()
        return redirect('liste_employes')
    return render(request,'employes/formulaire.html',{'form':form})

def  ModifierEmloyes(request,id):
    employer = get_object_or_404(Employer,id=id)
    form= formEmployes(request.POST or None,instance=employer)
    if form.is_valid():
        form.save()
        return redirect('liste_employes')
    return render(request, 'employes/formulaire.html', {'form': form})
    
def  SupprimerEmployer(request,id=id):
    supp= get_object_or_404(Employer,id=id)
    if request.method=="POST":
        supp.delete()
        return redirect('liste_employes')
    return render(request, 'employes/formulaire_confirm.html', {'supp': supp})
