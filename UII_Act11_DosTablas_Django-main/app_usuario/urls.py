from django.urls import path
from . import views

# Namespace de la aplicación para poder usar 'app_usuario:route_name' en templates
app_name = 'app_usuario'

urlpatterns = [
    # Ruta raíz
    path('', views.listar_usuarios, name='home'),
    
    # URLs de usuarios
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('usuarios/<int:usuario_id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:usuario_id>/borrar/', views.borrar_usuario, name='borrar_usuario'),

    # URLs de membresías
    path('membresias/', views.listar_membresias, name='listar_membresias'),
    path('membresias/crear/', views.crear_membresia, name='crear_membresia'),  # Asegurarse que este patrón está antes que los demás de membresías
    path('membresias/<int:membresia_id>/', views.detalle_membresia, name='detalle_membresia'),
    path('membresias/<int:membresia_id>/editar/', views.editar_membresia, name='editar_membresia'),
    path('membresias/<int:membresia_id>/borrar/', views.borrar_membresia, name='borrar_membresia'),
]
