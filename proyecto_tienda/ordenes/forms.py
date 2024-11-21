from django import forms
from .models import Orden
from productos.models import Producto
from .models import Cliente

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['producto', 'cantidad', 'cliente']
        producto = forms.ModelChoiceField(queryset=Producto.objects.all(), empty_label='Seleccione un producto')# el queryset es como decir SELECT * FROM en la bbdd (nos muestra todos los registros)
        cantidad = forms.IntegerField(min_value=1, initial=1)
        cliente  = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label='Seleccione un cliente')
        