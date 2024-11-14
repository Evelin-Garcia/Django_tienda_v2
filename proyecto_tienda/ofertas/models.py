from django.db import models
from django.forms import ValidationError
from productos.models import Producto

# Create your models here.

class Oferta(models.Model):
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    porcentaje_descuento=models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio=models.DateTimeField(null=False, blank=False)
    fecha_fin=models.DateTimeField(null=False, blank=False)
    
    #metodo especial para validaciones personalizadas en django (en este caso para fecha de inicio y porcentaje de descuento válidos)
    def clean(self): 
        if self.fecha_inicio>=self.fecha_fin:
            raise ValidationError("La fecha de inicio debe ser anterior a la de culminación") 
        if self.porcentaje_descuento<0 or self.porcentaje_descuento>100:
            raise ValidationError("El porcentaje de descuento debe estar entre 0% y 100%")
    
    #Llama a clean antes de guardar los datos en la bbdd y que los verifique previamente.    
    def save(self, *args, **kwargs):  #permite recibir cualquier argumento adicional necesario
        self.clean()
        super(Oferta, self).save(*args, **kwargs)
    
    #Este string se muestra en el panel de admin:
    def __str__(self):
        return f"Oferta en {self.producto.nombre} - {self.porcentaje_descuento}% de descuento" 
    
    #Calcula el precio de oferta:
    @property
    def precio_oferta(self):
        return self.producto.precio*(1-(self.porcentaje_descuento/100))
    
    