from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'main/index.html', context)

def classicgames(request):
    context={}
    return render(request, 'main/ClassicGames.html', context)

def classicgames2(request):
    context={}
    return render(request, 'main/ClassicGames2.html', context)

def contactanos(request):
    context={}
    return render(request, 'main/Contactanos.html', context)

def iniciarsesion(request):
    context={}
    return render(request, 'main/IniciarSesion.html', context)

def newgames(request):
    context={}
    return render(request, 'main/NewGames.html', context)

def newgames2(request):
    context={}
    return render(request, 'main/NewGames2.html', context)
    
def nosotros(request):
    context={}
    return render(request, 'main/Nosotros.html', context)

def registrarse(request):
    context={}
    return render(request, 'main/Registrarse.html', context)

def retrogames(request):
    context={}
    return render(request, 'main/RetroGames.html', context)

def retrogames2(request):
    context={}
    return render(request, 'main/RetroGames2.html', context)
    