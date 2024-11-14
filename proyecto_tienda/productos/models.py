from django.db import models

# Create your models here.       #acá creamos las tablas Categoría y Producto
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria =  models.ForeignKey (Categoria, on_delete=models.CASCADE)      
    
    def __str__(self):
        return self.nombre
    
    