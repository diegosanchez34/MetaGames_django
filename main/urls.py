from django.urls import path
from  . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('classicgames', views.classicgames, name='classicgames'),
    path('classicgames2', views.classicgames2, name='classicgames2'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('iniciarsesion', views.iniciarsesion, name='iniciarsesion'),
    path('newgames', views.newgames, name='newgames'),
    path('newgames2', views.newgames2, name='newgames2'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('retrogames', views.retrogames, name='retrogames'),
    path('retrogames2', views.retrogames2, name='retrogames2'),
    

    
]