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
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('admin')
    else:
        form = DestinationForm()
    return render(request, 'admin.html', {'form': form})
    