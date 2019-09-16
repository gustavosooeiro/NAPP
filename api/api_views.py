from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.exceptions import ValidationError
from api.serializers import ProdutoSerializer, ClienteSerializer, PedidoSerializer, ListaPedidoSerializer
from api.models import Produto, Cliente, Pedido
from rest_framework import viewsets, mixins

class ListaProdutos(ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ListaClientes(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_queryset(self):
        """Return objects ordered by name"""
        return self.queryset.all()
    
    def get_serializer_class(self):
        """Return apropriate serializer class"""
        print(self.action)
        if self.action in ('retrieve', 'list', 'update', 'partial_update'):
            return ListaPedidoSerializer
        return PedidoSerializer

    def perform_create(self, serializer):
        """Create a new Pedido"""
        serializer.save()