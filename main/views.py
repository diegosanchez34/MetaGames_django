from django.shortcuts import render, redirect
from .models import Juego,Categoria
from django.contrib import messages

# Create your views here.

def index(request):
    context={}
    return render(request, 'main/index.html', context)

def games(request):
    juegos = Juego.objects.all()
    context={"juegos":juegos}
    return render(request, 'main/games.html', context)

def classicgames(request):
    juegos = Juego.objects.all()
    context={"juegos":juegos}
    return render(request, 'main/ClassicGames.html', context)

def contactanos(request):
    context={}
    return render(request, 'main/Contactanos.html', context)

def iniciarsesion(request):
    context={}
    return render(request, 'main/IniciarSesion.html', context)

def newgames(request):
    juegos = Juego.objects.all()
    context={"juegos":juegos}
    return render(request, 'main/NewGames.html', context)
    
def nosotros(request):
    context={}
    return render(request, 'main/Nosotros.html', context)

def registrarse(request):
    context={}
    return render(request, 'main/Registrarse.html', context)

def retrogames(request):
    juegos = Juego.objects.all()
    context={"juegos":juegos}
    return render(request, 'main/RetroGames.html', context)


def crud(request):
    juegos = Juego.objects.all()
    categorias = Categoria.objects.all()
    context={"juegos":juegos,"categorias":categorias}
    return render(request, 'main/crud.html', context)

def agregar(request):
    categoria = request.POST['categoria']
    objCategoria = Categoria.objects.get(id = categoria)

    objJuego = Juego()
    objJuego.nombre = request.POST.get('nombre')
    objJuego.precio = request.POST.get('precio')
    objJuego.categoria = objCategoria
    
    if len(request.FILES) != 0:
        objJuego.image = request.FILES['image']
    
    objJuego.save()
    messages.success(request, 'Juego Agregado')
    return redirect('crud')

def eliminar(request, codigo):
    juego = Juego.objects.get(id=codigo)
    juego.delete()
    messages.success(request, 'Juego Eliminado')
    return redirect('crud')

def editar(request, codigo):
    juego = Juego.objects.get(id=codigo)
    categorias = Categoria.objects.all()
    context={"juego":juego,"categorias":categorias}
    return render(request, "main/editar.html", context)

def editarJuego(request):
    codigo = request.POST['id']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    categoria = request.POST['categoria']

    objCategoria = Categoria.objects.get(id = categoria)
    objJuego = Juego.objects.get(id=codigo)
    
    objJuego.nombre = nombre
    objJuego.categoria = objCategoria
    objJuego.precio = precio
    objJuego.save()

    messages.success(request, 'Juego actualizado')
    return redirect('crud')  