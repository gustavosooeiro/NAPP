from tastypie.resources import ModelResource
from api.models import Cliente, Produto, Pedido, ItensPedido
from tastypie.authorization import Authorization
from tastypie import fields
#from tastypie.validaton import Validation


""" class PedidoValidation(Validation):
    '''
    Make sure title and content are not empty
    '''
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'Não há dados nesse pedido.'}
        errors = {}
        if bundle.data.get('title', '') == '':
            errors['title'] = 'Title cannot be empty'
        if bundle.data.get('content', '') == '':
            errors['content'] = 'Content cannot be empty'
        return errors
 """

class ClienteResource(ModelResource):
    class Meta:
        queryset = Cliente.objects.all()
        resource_name = 'cliente'
        authorization = Authorization()
        fields = ['id', 'nome', 'resource_uri']
        list_allowed_methods= ['get']
        allowed_methods = ['get']

class ProdutoResource(ModelResource):
    class Meta:
        queryset = Produto.objects.all()
        resource_name = 'produto'
        authorization = Authorization()
        list_allowed_methods= ['get']
        allowed_methods = ['get']

class ItensPedidoResource(ModelResource):
    class Meta:
        queryset = ItensPedido.objects.all()
        resource_name = 'itens_pedido'
        authorization = Authorization()
        list_allowed_methods= ['get']
        allowed_methods = ['get']
        parent = "pedido"


class PedidoResource(ModelResource):
    #itens = fields.ToManyField(ItensPedidoResource, attribute=lambda bundle: ItensPedido.objects.filter(pedido=bundle.obj))
    itens = fields.ToManyField(ItensPedidoResource, 'pedido', full=True)
    class Meta:
        queryset = Pedido.objects.all()
        resource_name = 'pedido'
        authorization = Authorization()
        list_allowed_methods= ['get']
        allowed_methods = ['get', 'put']