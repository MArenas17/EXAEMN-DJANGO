from django.urls import path
from .import views

urlpatterns = [
    #URL DE PUBLICACION
    path('crearEmpleado/', views.crearEmpleado, name='crearEmpleado' ),
    path('verEmpleado/', views.verEmpleado, name='verEmpleado'),
    path('actualizarEmpleado/<int:id>', views.actualizarEmpleado, name='actualizarEmpleado'),
    path('eliminarEmpleado/<int:id>', views.eliminarEmpleado, name='eliminarEmpleado'),
]