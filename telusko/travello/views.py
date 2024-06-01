from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination
from .forms import DestinationForm, DeleteForm
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
    eliminar_form = DeleteForm()
    modificar_form = DestinationForm()
    destinos = Destination.objects.all()
    
    if request.method == 'POST':
        if 'crear' in request.POST:
            crear_form = DestinationForm(request.POST, request.FILES)
            if crear_form.is_valid():
                crear_form.save()
                return redirect('admin')
        elif 'eliminar' in request.POST:
            eliminar_form = DeleteForm(request.POST)
            if eliminar_form.is_valid():
                nombre_ciudad = eliminar_form.cleaned_data['nombreCiudad']
                destino = get_object_or_404(Destination, nombreCiudad=nombre_ciudad)
                destino.delete()
                return redirect('admin')
        elif 'modificar' in request.POST:
            
            pass
            
    
    context = {
        'crear_form': crear_form,
        'eliminar_form': eliminar_form,
        'modificar_form': modificar_form,
        'destinos': destinos,
    }
    return render(request, 'admin.html', context)
    