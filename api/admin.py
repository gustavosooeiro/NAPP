from django.contrib import admin
from api.models import Cliente, Produto, Pedido, ItensPedido
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_unitario', 'multiplo')


class PedidoDetalheInLine(admin.TabularInline):
    model = ItensPedido
    exclude = ['created']
    extra = 3

    def get_readonly_fields(self, request, obj=None):
        if obj: # obj is not None, so this is an edit
            return ['item','quantidade'] # Return a list or tuple of readonly fields' names
        else: # This is an addition
            return []

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):

    readonly_fields = ['detalhes']
    list_display = ('cliente', 'pedido_id', 'detalhes', 'total')
    inlines = [PedidoDetalheInLine]


#class CompraAdmin(admin.ModelAdmin):
    
#    fieldsets = [
#        #(None,               {'fields': ['parceiro_pj']}),
#        ('Date information', {'fields': ['createdat']}),
#        ('Compras',{'fields': ['parceiro_pj']}),
#    ]
#    list_display = ('parceiro_pj', 'createdat', 'detalhes', 'total')
#    inlines = [CompraDetalheInLine]
#    #short_description = "assfsdfsdfsd"