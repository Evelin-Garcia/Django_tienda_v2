from django.urls import path
from . import views


app_name= 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('cerrar_sesion/', views.logout_view, name='cerrar_sesion'),
    path('inicio_sesion/', views.login_view, name='login'),
]
