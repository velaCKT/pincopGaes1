from django.contrib import admin
from .models import Producto, Transaccion, ImagenProducto
from babel.numbers import format_currency
from django.db.models import Sum


class TransaccionInline(admin.TabularInline):
    model = Transaccion
    extra = 0


class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1 


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'talla', 'modelo', 'categoria', 'precio_colombiano', 'cantidad')
    list_filter = ('marca', 'talla', 'categoria')
    search_fields = ('marca__descripcion', 'talla__nro_talla', 'modelo', 'categoria__descripcion')
    inlines = [TransaccionInline, ImagenProductoInline]  # Combine inlines into one line

    def precio_colombiano(self, obj):
        return format_currency(obj.precio, 'COP', locale='es_CO')
    precio_colombiano.short_description = 'Precio (COP)'

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj=obj)
        field_order = ('marca', 'modelo', 'categoria', 'descripcion', 'talla', 'cantidad', 'precio')
        fieldsets[0][1]['fields'] = field_order
        return fieldsets

    actions = ['calcular_inventario']

    def calcular_inventario(self, request, queryset):
        inventario_disponible = queryset.aggregate(total=Sum('cantidad'))['total'] or 0
        self.message_user(request, f'El inventario total disponible es: {inventario_disponible}')
    calcular_inventario.short_description = "Calcular inventario disponible"
