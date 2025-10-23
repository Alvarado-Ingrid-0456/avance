from django import forms
from .models import Usuario, Membresia

# --- FORMULARIO DE USUARIOS ---
class UsuarioForm(forms.ModelForm):
    contrasena_hash = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña'
        })
    )

    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'email',
            'contrasena_hash',
            'avatar',
            'es_creador'
        ]
        labels = {
            'nombre_usuario': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'avatar': 'Avatar (imagen)',
            'es_creador': '¿Es creador de contenido?',
        }
        widgets = {
            'nombre_usuario': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: comicfan01'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com'
            }),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'es_creador': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# --- FORMULARIO DE MEMBRESÍAS ---
class MembresiaForm(forms.ModelForm):
    class Meta:
        model = Membresia
        fields = [
            'usuario',
            'tipo_membresia',
            'fecha_expiracion',
            'precio',
            'estado'
        ]
        labels = {
            'usuario': 'Usuario',
            'tipo_membresia': 'Tipo de Membresía',
            'fecha_expiracion': 'Fecha de Expiración',
            'precio': 'Precio (MXN)',
            'estado': 'Activa',
        }
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'tipo_membresia': forms.Select(attrs={'class': 'form-control'}),
            'fecha_expiracion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
