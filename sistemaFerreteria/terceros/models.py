# terceros/models.py
from django.db import models

class Cliente(models.Model):
    """
    Modelo para la gestión de la cartera de clientes.
    """
    TIPO_DOCUMENTO_CHOICES = [
        ('DNI', 'DNI'),
        ('RUC', 'RUC'),
        ('OTRO', 'Otro'),
    ]

    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre/Razón Social")
    tipo_documento = models.CharField(max_length=4, choices=TIPO_DOCUMENTO_CHOICES, default='DNI')
    num_documento = models.CharField(max_length=15, unique=True, verbose_name="N° Documento")
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre_completo

class Proveedor(models.Model):
    """
    Modelo para la gestión de proveedores.
    """
    razon_social = models.CharField(max_length=150, unique=True)
    ruc = models.CharField(max_length=15, unique=True, verbose_name="RUC")
    nombre_contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=200)
    descripcion_productos = models.TextField(verbose_name="Productos que ofrece", blank=True, null=True)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.razon_social
