from .models import Produto, Cliente, Pedido, ItensPedido
from rest_framework import serializers

class ProdutoSerializer(serializers.ModelSerializer):
    preco_unitario = serializers.DecimalField(min_value=0.01, decimal_places=2, max_digits=22)
    class Meta:
        model=Produto
        fields=('id', 'nome', 'preco_unitario', 'multiplo')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=('id', 'nome')

class ItensPedidoSerializer(serializers.ModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(many=False, queryset=Produto.objects.all())
    preco = serializers.DecimalField(min_value=0.01, decimal_places=2, max_digits=22, coerce_to_string=False)
    class Meta:
        model=ItensPedido
        fields=('pedido', 'produto', 'preco', 'quantidade')

class ListaPedidoSerializer(serializers.ModelSerializer):

    cliente = ClienteSerializer
    produtos = serializers.SerializerMethodField()

    total = serializers.DecimalField(max_digits=22, decimal_places=2, read_only=True) #CharField(min_length=2, max_length=30, read_only=True)

    class Meta:
        model=Pedido
        fields=('id', 'cliente', 'total', 'produtos')

    def get_produtos(self, instance):
        items = ItensPedido.objects.filter(pedido=instance)
        return ItensPedidoSerializer(items, many=True).data

class PedidoSerializer(ListaPedidoSerializer):
    
    cliente = serializers.PrimaryKeyRelatedField(many=False, queryset=Cliente.objects.all())
    produtos = ItensPedidoSerializer(many=True)

    def create(self, validated_data):
        cliente_dados = validated_data['cliente']
        produtos_dados = validated_data['produtos']

        try:
            if not produtos_dados:
                raise ValidationError({'produtos': 'Pelo menos um produto é necessário!'})
        except ValueError:
            raise ValidationError({'produtos': 'Deve ser um produto já cadastrado!'})
        
        pedido, created = Pedido.objects.create(cliente=cliente_dados)
        for produto_dados in produtos_dados:
            print(produto_dados)
            ItensPedido.objects.create(pedido=pedido, **produto_dados)
        return pedido


