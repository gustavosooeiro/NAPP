from .models import Produto, Cliente, Pedido, ItensPedido
from rest_framework import serializers
from .validations import valida_produtos, valida_multiplo, verifica_rentabilidade

class ProdutoSerializer(serializers.ModelSerializer):
    """Produto serializer"""
    preco_unitario = serializers.DecimalField(min_value=0.01, decimal_places=2, max_digits=22)
    class Meta:
        model=Produto
        fields=('id', 'nome', 'preco_unitario', 'multiplo')

class ClienteSerializer(serializers.ModelSerializer):
    """Cliente serializer"""
    class Meta:
        model=Cliente
        fields=('id', 'nome')

class ItensPedidoSerializer(serializers.ModelSerializer):
    """Itens Pedido serializer"""
    produto = serializers.PrimaryKeyRelatedField(many=False, queryset=Produto.objects.all())
    preco = serializers.DecimalField(min_value=0.00, decimal_places=2, max_digits=22)
    quantidade = serializers.IntegerField(required=True, min_value=1, error_messages={
            "null": "Quantidade não pode ser null.",
            "min_value": "Quantidade mínima é 1.",
    })

    rentabilidade = serializers.SerializerMethodField()

    class Meta:
        model=ItensPedido
        fields=('produto', 'preco', 'quantidade', 'rentabilidade')


    def get_rentabilidade(self, instance):

        return verifica_rentabilidade(instance.produto.id, 
                                    instance.produto.nome, 
                                    instance.preco, 
                                    instance.produto.preco_unitario, 
                                    False)

<<<<<<< HEAD
class PedidoSerializer(ListaPedidoSerializer):
    
    produtos = ItensPedidoSerializer(many=True)
        
=======
class PedidoSerializer(serializers.ModelSerializer):
    """Pedido serializer para operações de POST"""
    cliente = serializers.PrimaryKeyRelatedField(many=False, queryset=Cliente.objects.all())
    produtos = ItensPedidoSerializer(many=True)
    total = serializers.DecimalField(max_digits=22, decimal_places=2, read_only=True) #CharField(min_length=2, max_length=30, read_only=True)

    class Meta:
        model=Pedido
        fields=('id', 'cliente', 'total', 'produtos')

>>>>>>> using-viewset
    def create(self, validated_data):
        cliente_dados = validated_data['cliente']
        produtos_dados = validated_data['produtos']

        #validação dos produtos
        valida_produtos(produtos_dados)

        
<<<<<<< HEAD
        pedido = Pedido.objects.create(cliente=cliente_dados)
        for produto_dados in produtos_dados:
            ItensPedido.objects.create(pedido=pedido, **produto_dados)
        self.produtos = super().get_produtos(pedido)
        return pedido
=======
        for produto_dados in produtos_dados:
            quantidade = produto_dados['quantidade']
            preco = produto_dados['preco']
            id_produto = produto_dados['produto'].id
            nome_produto = produto_dados['produto'].nome
            preco_produto = produto_dados['produto'].preco_unitario
            multiplo = produto_dados['produto'].multiplo

            #validação de quantidades(de acordo com o múltiplo) para cada item do pedido
            if (multiplo):
                valida_multiplo(id_produto, nome_produto, quantidade, multiplo)
            
            #validação de rentabilidade de cada item do pedido
            verifica_rentabilidade(id_produto, 
                                nome_produto, 
                                preco, 
                                preco_produto, 
                                True)

        pedido = Pedido.objects.create(cliente=cliente_dados)

        for produto_dados in produtos_dados:
            ItensPedido.objects.create(pedido=pedido, **produto_dados)
        
        pedido.produtos = ItensPedido.objects.filter(pedido=pedido)        
        return pedido


class ListaPedidoSerializer(PedidoSerializer):
    """Pedido serializer para operações de Listagem"""

    cliente = ClienteSerializer()
    produtos = serializers.SerializerMethodField()

    def get_produtos(self, instance):
        items = ItensPedido.objects.filter(pedido=instance)
        return ItensPedidoSerializer(items, many=True).data

>>>>>>> using-viewset
