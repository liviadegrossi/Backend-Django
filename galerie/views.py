from django.shortcuts import render, get_object_or_404
from galerie.models import Photograph

def index(request):
    # photos = Photograph.objects.all()
    photos = Photograph.objects.order_by("date").filter(published=True)
    return render(request, 'galerie/index.html', {'cards': photos})

def imagem(request, photo_id):
    photo = get_object_or_404(Photograph, pk=photo_id)
    return render(request, 'galerie/imagem.html', {"photo": photo})