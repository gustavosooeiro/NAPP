from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.exceptions import ValidationError
from api.serializers import ProdutoSerializer, ClienteSerializer, PedidoSerializer, ListaPedidoSerializer
from api.models import Produto, Cliente, Pedido

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

class CriaPedido(ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    
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