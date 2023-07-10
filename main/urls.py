from django.urls import path
from  . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('games', views.games, name='games'),
    path('classicgames', views.classicgames, name='classicgames'),
    path('newgames', views.newgames, name='newgames'),
    path('retrogames', views.retrogames, name='retrogames'),
    path('crud', views.crud, name='crud'),
    path('agregar/', views.agregar, name='agregar'),
    path('eliminar/<codigo>', views.eliminar, name='eliminar'),
    path('editar/<codigo>', views.editar, name='editar'),
    path('editarJuego/', views.editarJuego),
    path('login/', views.login),
    path('register/', views.register),
    path('iniciarsesion', views.iniciarsesion, name='iniciarsesion'),  
    path('registrarse', views.registrarse, name='registrarse'),
]