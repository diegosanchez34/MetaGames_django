from django.urls import path
from  . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('main/ClassicGames.html', views.classicgames, name='classicgames'),
    path('main/ClassicGames2.html', views.classicgames2, name='classicgames2'),
    path('main/Contactanos.html', views.contactanos, name='contactanos'),
    path('main/IniciarSesion.html', views.iniciarsesion, name='iniciarsesion'),
    path('main/NewGames.html', views.newgames, name='newgames'),
    path('main/NewGames2.html', views.newgames2, name='newgames2'),
    path('main/Nosotros.html', views.nosotros, name='nosotros'),
    path('main/Registrarse.html', views.registrarse, name='registrarse'),
    path('main/RetroGames.html', views.retrogames, name='retrogames'),
    path('main/RetroGames2.html', views.retrogames2, name='retrogames2'),
    

    
]