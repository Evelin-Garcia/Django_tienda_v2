from django.shortcuts import get_object_or_404, render, redirect
from .forms import OrdenForm
from .models import Orden

# Create your views here.
def crear_orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ordenes:ver_ordenes')
    else:
        form = OrdenForm()
    return render(request, 'ordenes/crear_orden.html', {'form':form})

def editar_orden(request, orden_id):
    orden = get_object_or_404(Orden, pk=orden_id)

    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('ordenes:ver_ordenes')
    else:
        form = OrdenForm(instance=orden)
    return render(request, 'ordenes/crear_orden.html', {'form':form})

def eliminar_orden(request, orden_id):
    orden = get_object_or_404(Orden, pk = orden_id)

    if request.method == 'POST':
        orden.delete()
        return redirect('ordenes:ver_ordenes')
    return render(request, 'ordenes/eliminar_orden.html', {'orden': orden})

def ver_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'ordenes/ver_ordenes.html', {'ordenes': ordenes})