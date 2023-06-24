from django.contrib import admin
from .models import Juego,Categoria

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Juego)