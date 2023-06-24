from django.shortcuts import render, redirect
from .models import Juego,Categoria
from django.contrib import messages

# Create your views here.

def index(request):
    context={}
    return render(request, 'main/index.html', context)

def games(request):
    context={}
    return render(request, 'main/games.html', context)

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

def crud(request):
    juegos = Juego.objects.all()
    categorias = Categoria.objects.all()
    context={"juegos":juegos,"categorias":categorias}
    return render(request, 'main/crud.html', context)

def agregar(request):
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    categoria = request.POST['categoria']

    objCategoria = Categoria.objects.get(id = categoria)
    objJuego = Juego.objects.create(nombre=nombre, categoria=objCategoria, precio=precio)
    messages.success(request, '¡Juego Agregado!')
    return redirect('crud')

def eliminar(request, codigo):
    juego = Juego.objects.get(id=codigo)
    juego.delete()
    messages.success(request, 'Juego Eliminado')
    return redirect('crud')

def editar(request, codigo):
    juego = Juego.objects.get(id=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})




def editar(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/')

    