from .models import Produto, Cliente, Pedido, ItensPedido
from rest_framework import serializers

class ProdutoSerializer(serializers.ModelSerializer):
    preco_unitario = serializers.DecimalField(min_value=0.01, decimal_places=2, max_digits=None)
    class Meta:
        model=Produto
        fields=('id', 'nome', 'preco_unitario', 'multiplo')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=('id', 'nome')

class ItensPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItensPedido
        fields=('pedido', 'produto', 'preco', 'quantidade')

class PedidoSerializer(serializers.ModelSerializer):
    #itens_set=ItensPedidoSerializer(many=True)
    cliente = serializers.CharField(source='cliente.nome')
    produtos = serializers.SerializerMethodField()
    
    total = serializers.CharField(min_length=2, max_length=30, read_only=True)

    class Meta:
        model=Pedido
        fields=('id', 'cliente', 'pedido_id', 'status_pagamento', 'total', 'produtos') 

    def get_produtos(self, instance):
        items = ItensPedido.objects.filter(pedido=instance)
        return ItensPedidoSerializer(items, many=True).data

