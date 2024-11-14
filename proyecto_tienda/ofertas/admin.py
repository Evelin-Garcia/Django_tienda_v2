from django.contrib import admin
from .models import Oferta

# Register your models here.
@admin.register(Oferta)

class OfertaAdmin(admin.ModelAdmin):
    list_display=('producto', 'porcentaje_descuento', 'fecha_inicio', 'fecha_fin') #list display es una propiedad que indica lo que se mostrará en administracion para las columnas 
    search_fields=('producto__nombre', ) #idem con search fields que mostrará el campo de búsqueda de nombre en el panel de administración.
    
    