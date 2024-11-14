from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Oferta
from .forms import OfertaForm
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    current_date=datetime.now()
    ofertas=[]
    
    try:
        ofertas=Oferta.objects.filter(fecha_inicio__lte=current_date, fecha_fin__gte=current_date) 
#        raise Exception("Simulación de error inesperado")  #Esta línea se hizo para probar que el 
#error inesperado del bloque try except está funcionando, debe mantenerse comentada.
        if not ofertas:
            raise ValueError("No hay ofertas disponibles en este momento")
    except ValueError as e:
        #Manejo de error específico (no hay ofertas)
        return render(request, 'ofertas/index.html', {'error': str(e), 'current_date': current_date})
    except Exception as e:
        #Manejo de cualquier otro error
        return render(request, 'ofertas/index.html', {'error': 'Se produjo un error inesperado!', 'current_date': current_date})
    
    context={
#        'is_special_offer': False  #Se Cambia a True para si y False para no (para que aparezca si o no)        
        'current_date':current_date,
        'ofertas':ofertas
    }
    return render(request, 'ofertas/index.html', context)



@login_required()
@permission_required('ofertas.add_oferta', raise_exception=True)
#funcion para el formulario de ofertas
def crear_oferta(request):
    if request.method=='POST':
        form=OfertaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ofertas:index')
    else:
        form=OfertaForm()
    return render(request, 'ofertas/crear_oferta.html', {'form':form})

@login_required()
@permission_required('ofertas.change_oferta', raise_exception=True)
def editar_oferta(request, oferta_id):
    oferta= get_object_or_404(Oferta, id=oferta_id)
    if request.method == 'POST':
        form=OfertaForm(request.POST, instance=oferta)
        if form.is_valid():
            form.save()
            return redirect('ofertas:index')
    else:
        form=OfertaForm(instance=oferta)    
    return render(request, 'ofertas/crear_oferta.html', {'form':form}) #Crear html de editar oferta y de eliminar oferta

@login_required()
@permission_required('ofertas.delete_oferta', raise_exception=True)
def eliminar_oferta(request, oferta_id):
    oferta = get_object_or_404(Oferta, id=oferta_id)
    if request.method=='POST':
        oferta.delete()
        return redirect('ofertas:index')
    return render(request, 'ofertas/eliminar_oferta.html', {'oferta':oferta}) 
    


    

