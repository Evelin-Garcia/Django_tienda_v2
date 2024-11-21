from django.db import models
from productos.models import Producto

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    
    def __str__(self):
        return self.nombre

class Orden(models.Model):
    n_orden = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_orden = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs): #sobreescribe un método en este caso Orden sobre escribe models con los datos que le damos
        self.precio_unitario = self.producto.precio
        self.total = self.precio_unitario*self.cantidad
        super().save(*args, **kwargs) #es una forma para pasar cualquier cantidad de argumentos sin tener q definirlos especificamente, al guardarlos
        
    def __str__(self):
        return f'N° orden: {self.n_orden}, Producto: {self.producto.nombre}'    