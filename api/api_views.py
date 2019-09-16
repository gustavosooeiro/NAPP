from rest_framework.generics import ListAPIView
from api.serializers import ProdutoSerializer, ClienteSerializer, PedidoSerializer, ListaPedidoSerializer
from api.models import Produto, Cliente, Pedido
from rest_framework import viewsets

class ListaProdutos(ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ListaClientes(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

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