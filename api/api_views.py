<<<<<<< HEAD
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.exceptions import ValidationError
=======
from rest_framework.generics import ListAPIView
>>>>>>> using-viewset
from api.serializers import ProdutoSerializer, ClienteSerializer, PedidoSerializer, ListaPedidoSerializer
from api.models import Produto, Cliente, Pedido
from rest_framework import viewsets

class ListaProdutos(ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ListaClientes(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

<<<<<<< HEAD
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
=======
class PedidoViewSet(viewsets.ModelViewSet):
    """Gerencia Pedidos no banco de dados"""
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_queryset(self):
        """Retorna os objetos"""
        return self.queryset.all()
    
    def get_serializer_class(self):
        """Retorna os serializers mais apropriados"""
        if self.action in ('retrieve', 'list', 'update', 'partial_update'):
            return ListaPedidoSerializer
        return PedidoSerializer

    def perform_create(self, serializer):
        """Cria um novo Pedido"""
        serializer.save()
>>>>>>> using-viewset
