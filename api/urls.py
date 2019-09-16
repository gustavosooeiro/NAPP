from django.urls import path, include

from .api_views import PedidoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pedidos', PedidoViewSet)

urlpatterns = [ 
    path('', include(router.urls))
]
