from django.shortcuts import render, redirect
from .models import Destination
from .forms import DestinationForm
# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Perú'
    return render(request, 'index.html', {'dest1': dest1});

def about(request):
    return render(request, 'about.html');
    
def contact(request):
    return render(request, 'contact.html');
    
def news(request):
    return render(request, 'news.html');
    
def admin(request):
    crear_form = DestinationForm()
    eliminar_form = DestinationForm()
    modificar_form = DestinationForm()
    listar_form = DestinationForm()
    
    if request.method == 'POST':
        if 'crear' in request.POST:
            crear_form = DestinationForm(request.POST, request.FILES)
            if crear_form.is_valid():
                crear_form.save()
                return redirect('admin')
        elif 'eliminar' in request.POST:
            
            pass
        elif 'modificar' in request.POST:
            
            pass
        elif 'listar' in request.POST:
            
            pass
    
    context = {
        'crear_form': crear_form,
        'eliminar_form': eliminar_form,
        'modificar_form': modificar_form,
        'listar_form': listar_form,
    }
    return render(request, 'admin.html', context)
    