from django.urls import path, include

from .api_views import ListaClientes, ListaProdutos, ListaPedidos, CriaPedido, PedidoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pedidos', PedidoViewSet)

app_name = 'api'

urlpatterns = [ 
    path('', include(router.urls))
]

#urlpatterns = [ 
#    path('clientes/', ListaClientes.as_view(), name='clientes'),
#    path('produtos/', ListaProdutos.as_view(), name='produtos'),
 #   path('pedidos/', ListaPedidos.as_view(), name='clientes'),
 #   path('pedido/novo', CriaPedido.as_view(), name='pedido_novo')
#]