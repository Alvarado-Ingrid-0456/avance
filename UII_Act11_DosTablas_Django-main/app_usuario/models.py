from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    contrasena_hash = models.CharField(max_length=255)
    fecha_registro = models.DateField(default=timezone.now)
    ultima_conexion = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    es_creador = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre_usuario} ({'Creador' if self.es_creador else 'Lector'})"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['nombre_usuario']  # ejemplo: orden al listar


class Membresia(models.Model):
    TIPOS_MEMBRESIA = [
        ('BASICA', 'Básica'),
        ('PREMIUM', 'Premium'),
        ('VIP', 'VIP'),
    ]

    id_membresia = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name='membresia'
    )
    tipo_membresia = models.CharField(
        max_length=10,
        choices=TIPOS_MEMBRESIA,
        default='BASICA'
    )
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_expiracion = models.DateField(null=True, blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Membresía {self.tipo_membresia} de {self.usuario.nombre_usuario}"

    class Meta:
        verbose_name = "Membresía"
        verbose_name_plural = "Membresías"
        ordering = ['-fecha_inicio']  # ejemplo: más recientes primero
