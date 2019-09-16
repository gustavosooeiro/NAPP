from django.urls import path, include

from .api_views import PedidoViewSet, ListaClientes, ListaProdutos
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pedidos', PedidoViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
    path('clientes/', ListaClientes.as_view()),
    path('produtos/', ListaProdutos.as_view()),
]
