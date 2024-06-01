from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Perú'
    return render(request, 'index.html', {'dest1': dest1});

def about(request):
    return render(request, 'about.html');
    
def contact(request):
    return render(request, 'contact.html');