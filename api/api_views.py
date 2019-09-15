from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.exceptions import ValidationError
from api.serializers import ProdutoSerializer, ClienteSerializer, PedidoSerializer, ListaPedidoSerializer
from api.models import Produto, Cliente, Pedido
from rest_framework import viewsets

class ListaProdutos(ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    #filter_backends = (DjangoFilterBackend, SearchFilter)
    #filter_fields = ('id',)
    #search_fields = ('id', 'nome')

class ListaClientes(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ListaPedidos(ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = ListaPedidoSerializer

class CriaPedido(CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    allowed_methods=['GET', 'POST', 'HEAD', 'OPTIONS']

    def get_queryset(self):
        """Return objects ordered by name"""
        return self.queryset.all()
    
    def get_serializer_class(self):
        """Return apropriate serializer class"""
        print(self.action)
        if self.action in ('retrieve', 'list', 'create'):
            print("rntrou")
            return ListaPedidoSerializer
        print("saiu")
        return PedidoSerializer

'''
    def create(self, request, *args, **kwargs):
        try: 
            preco = request.data.get('preco'):
            if preco is not None and float(preco) >= 0.0:
                raise ValidationError({'preco': 'Deve ser maior que R$ 0,00'})
        except ValueError:
            raise ValidationError({'preco': 'Deve ser um número válido'})
        return super().create(self, request, *args, **kwargs)
'''