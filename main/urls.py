from django.urls import path
from  . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('classicgames', views.classicgames, name='classicgames'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('iniciarsesion', views.iniciarsesion, name='iniciarsesion'),
    path('newgames', views.newgames, name='newgames'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('retrogames', views.retrogames, name='retrogames'),
    path('games', views.games, name='games'),
    path('crud', views.crud, name='crud'),
    path('agregar/', views.agregar, name='agregar'),
    path('eliminar/<codigo>', views.eliminar, name='eliminar'),
    path('editar/<codigo>', views.editar, name='editar'),
    path('editarJuego/', views.editarJuego)    
]