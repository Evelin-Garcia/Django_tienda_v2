from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [
    path('', views.ver_ordenes, name='ver_ordenes'),
    path('crear/', views.crear_orden, name='crear_orden'),
    path('eliminar/<int:orden_id>/', views.eliminar_orden, name='eliminar_orden'),
    path('editar/<int:orden_id>/', views.editar_orden, name='editar_orden'),
]
