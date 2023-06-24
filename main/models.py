from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(db_column='idCategoria', primary_key=True) 
    nombre = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        texto = "({0}) {1}"
        return texto.format(self.id, self.nombre)

class Juego(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')
    precio = models.IntegerField() 

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.nombre)