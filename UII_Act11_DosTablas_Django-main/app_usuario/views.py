from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Membresia
from .forms import UsuarioForm, MembresiaForm

# Create your views here.

# -------------------------------
# VISTAS DE USUARIOS
# -------------------------------
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})


def detalle_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    return render(request, 'usuarios/detalle_usuario.html', {'usuario': usuario})


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_usuario:listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/formulario_usuario.html', {
        'form': form,
        'titulo': 'Crear Usuario'
    })


def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('app_usuario:detalle_usuario', usuario_id=usuario.id_usuario)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/formulario_usuario.html', {
        'form': form,
        'titulo': 'Editar Usuario'
    })


def borrar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('app_usuario:listar_usuarios')
    return render(request, 'usuarios/confirmar_borrar.html', {'usuario': usuario})


# -------------------------------
# VISTAS DE MEMBRESÍAS
# -------------------------------
def listar_membresias(request):
    membresias = Membresia.objects.all()
    return render(request, 'membresias/listar_membresias.html', {'membresias': membresias})


def detalle_membresia(request, membresia_id):
    membresia = get_object_or_404(Membresia, id_membresia=membresia_id)
    return render(request, 'membresias/detalle_membresia.html', {'membresia': membresia})


def crear_membresia(request):
    print("DEBUG: Entrando a crear_membresia, método:", request.method)  # Debug print
    if request.method == 'POST':
        form = MembresiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_usuario:listar_membresias')
    else:
        form = MembresiaForm()
    return render(request, 'membresias/formulario_membresia.html', {
        'form': form,
        'titulo': 'Crear Membresía'
    })


def editar_membresia(request, membresia_id):
    membresia = get_object_or_404(Membresia, id_membresia=membresia_id)
    if request.method == 'POST':
        form = MembresiaForm(request.POST, request.FILES, instance=membresia)
        if form.is_valid():
            form.save()
            return redirect('app_usuario:detalle_membresia', membresia_id=membresia.id_membresia)
    else:
        form = MembresiaForm(instance=membresia)
    return render(request, 'membresias/formulario_membresia.html', {
        'form': form,
        'titulo': 'Editar Membresía'
    })


def borrar_membresia(request, membresia_id):
    membresia = get_object_or_404(Membresia, id_membresia=membresia_id)
    if request.method == 'POST':
        membresia.delete()
        return redirect('app_usuario:listar_membresias')
    return render(request, 'membresias/confirmar_borrar.html', {'membresia': membresia})
