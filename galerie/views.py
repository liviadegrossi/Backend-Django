from django.shortcuts import render

def index(request):
    data = {
        1: {'name': 'Nebulosa de Carina',
            'legend': 'webbtelescope.org / NASA / James Webb'
        },
        2: {'name': 'Galáxia NGC 1079',
            'legend': 'nasa.org / NASA / Hubble'
        }
    }
    return render(request, 'galerie/index.html', {'cards': data})

def imagem(request):
    return render(request, 'galerie/imagem.html')