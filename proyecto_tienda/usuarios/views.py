from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .forms import RegistroForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            #asignación del nuevo usuario al grupo comun
            grupo_usuario_comun = Group.objects.get(name='Usuario_comun')
            user.groups.add(grupo_usuario_comun)
            return redirect('usuarios:login')
    else:
        form = RegistroForm()
        return render(request, 'usuarios/registro.html', {'form':form})  
    
              
#cierra la sesion de usuario y redirigue a la página de inicio
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada con éxito')
    return redirect('usuarios:login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, 'Inicio de Sesión exitoso')
            return redirect('productos:index')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form':form})
