from django.shortcuts import render
from .models import Alumno,Genero
# Create your views here.


def index(request):
    context={}
    return render(request,'main/index.html',context)

def nosotros(request):
    context={}
    return render(request,'main/Nosotros.html',context)

def retrogames(request):
    context={}
    return render(request,'main/RetroGames.html',context)

def retrogames2(request):
    context={}
    return render(request,'main/RetroGames2.html',context)

def iniciarsesion(request):
    context={}
    return render(request,'main/IniciarSesion.html',context)

def registrarse(request):
    context={}
    return render(request,'main/Registrarse.html',context)

def newgames(request):
    context={}
    return render(request,'main/NewGames.html',context)

def newgames2(request):
    context={}
    return render(request,'main/NewGames2.html',context)

def classicgames(request):
    context={}
    return render(request,'main/ClassicGames.html',context)

def classicgames2(request):
    context={}
    return render(request,'main/ClassicGames2.html',context)

def contactanos(request):
    context={}
    return render(request,'main/Contactanos.html',context)

def index(request):
    alumnos = Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request,'ongapp/index.html',context)


def listadoSQL(request):
    alumnos= Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    print(alumnos)
    context={"alumnos":alumnos}
    return render(request,'ongapp/listadoSQL.html',context)

