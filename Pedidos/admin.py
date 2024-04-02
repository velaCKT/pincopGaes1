from django.contrib import admin
from .models import Pedido, DetallePedido

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_pedido', 'estado')
    list_filter = ('estado',)
    search_fields = ('cliente__username',)
    inlines = [DetallePedidoInline]
    actions = ['confirmar_pedido', 'enviar_pedido', 'marcar_como_entregado', 'cancelar_pedido']

    def confirmar_pedido(self, request, queryset):
        queryset.update(estado='confirmado')
    confirmar_pedido.short_description = "Confirmar pedido"

    def enviar_pedido(self, request, queryset):
        queryset.update(estado='enviado')
    enviar_pedido.short_description = "Enviar pedido"

    def marcar_como_entregado(self, request, queryset):
        queryset.update(estado='entregado')
    marcar_como_entregado.short_description = "Marcar como entregado"

    def cancelar_pedido(self, request, queryset):
        queryset.update(estado='cancelado')
    cancelar_pedido.short_description = "Cancelar pedido"
