from django.db.models import Sum
from .models import Producto

def crear_producto(nombre, descripcion, cantidad_disponible, precio):
    producto = Producto.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        cantidad_disponible=cantidad_disponible,
        precio=precio
    )
    return producto

def actualizar_producto(id_producto, nombre, descripcion, cantidad_disponible, precio):
    try:
        producto = Producto.objects.get(pk=id_producto)
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.cantidad_disponible = cantidad_disponible
        producto.precio = precio
        producto.save()
        return producto
    except Producto.DoesNotExist:
        return None

def eliminar_producto(id_producto):
    try:
        producto = Producto.objects.get(pk=id_producto)
        producto.delete()
        return True
    except Producto.DoesNotExist:
        return False

def calcular_inventario_disponible():
    inventario_disponible = Producto.objects.aggregate(total=Sum('cantidad_disponible'))
    return inventario_disponible['total'] if inventario_disponible['total'] is not None else 0 
