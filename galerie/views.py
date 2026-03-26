from django.shortcuts import render, get_object_or_404, redirect
from galerie.models import Photograph
from django.contrib import messages

def index(request):
    # photos = Photograph.objects.all()

    # check whether the user is authenticated
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    photos = Photograph.objects.order_by("date").filter(published=True)
    return render(request, 'galerie/index.html', {'cards': photos})

def imagem(request, photo_id):
    photo = get_object_or_404(Photograph, pk=photo_id)
    return render(request, 'galerie/imagem.html', {"photo": photo})

def search(request):

    # check whether the user is authenticated
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    photos = Photograph.objects.order_by('date').filter(published=True)

    # check whether the search term is in the request
    if 'search' in request.GET: 
        # get the search term in the request URL
        name_to_search = request.GET['search'] # search is the name used in the input tag of the menu
        # if there is a term to search, filter the photos by it
        if name_to_search: 
            photos = photos.filter(name__icontains=name_to_search)

    return render(request, 'galerie/search.html', {'cards': photos})