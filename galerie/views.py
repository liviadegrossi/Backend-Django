from django.shortcuts import render
from galerie.models import Photograph

def index(request):
    photos = Photograph.objects.all()
    return render(request, 'galerie/index.html', {'cards': photos})

def imagem(request):
    return render(request, 'galerie/imagem.html')