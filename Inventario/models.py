from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.core.validators import MinValueValidator
from babel.numbers import format_currency
        
class Marca(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Talla(models.Model):
    nro_talla = models.CharField(max_length=20)

    def __str__(self):
        return self.nro_talla

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class ImagenProducto(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos')
    
class Producto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.modelo} - {self.marca} - {self.talla} - {self.categoria}'
    
    @classmethod
    def precio_with_currency(cls, precio):
        return format_currency(precio, 'COP', locale='es_CO')
    
    def registrar_entrada(self, cantidad_entrada):
        self.cantidad += cantidad_entrada
        self.save()
        Transaccion.objects.create(
            producto=self,
            tipo='Entrada',
            cantidad=cantidad_entrada,
            fecha=timezone.now()
        )

    def registrar_salida(self, cantidad_salida):
        if self.cantidad >= cantidad_salida:
            self.cantidad -= cantidad_salida
            self.save()
            Transaccion.objects.create(
                producto=self,
                tipo='Salida',
                cantidad=cantidad_salida,
                fecha=timezone.now()
            )
        else:
            raise ValueError('La cantidad de salida es mayor que la cantidad disponible')


class Transaccion(models.Model):
    TIPOS_TRANSACCION = [
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida')
    ]      
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPOS_TRANSACCION)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField()

    class Meta:
        verbose_name = 'Transacción'  
        verbose_name_plural = 'Transacciones'

