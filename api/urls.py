from django.urls import path, include

from .api_views import ListaClientes, ListaProdutos, ListaPedidos, CriaPedido

urlpatterns = [ 
    path('clientes/', ListaClientes.as_view(), name='clientes'),
    path('produtos/', ListaProdutos.as_view(), name='produtos'),
    path('pedidos/', ListaPedidos.as_view(), name='clientes'),
    path('pedido/novo', CriaPedido.as_view(), name='pedido_novo')
]