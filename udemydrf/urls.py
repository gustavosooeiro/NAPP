from django.contrib import admin
from django.urls import path, include
from api.api_views import ListaClientes, ListaProdutos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]
