from rest_framework.exceptions import ValidationError
from .models import Produto
from decimal import Decimal

def valida_produtos(produtos):
    """Valida se existe pelo menos um produto existe"""
    try:
        if not produtos:
            raise ValidationError({'produtos': 'Pelo menos um produto é necessário!'})
    except ValueError:
        raise ValidationError({'produtos': 'Erro com produtos!'})


def valida_multiplo(id_produto, nome_produto, quantidade, multiplo):
    """Cada item do pedido deve conter quantidade divisível pelo seu múltiplo"""
    if(quantidade % multiplo!=0):
        mensagem = 'A quantidade do produto ({}:{}), deve ser múltiplo de {}'.format(
            id_produto,
            nome_produto,
            multiplo)
        raise ValidationError({'item do pedido': mensagem})

def verifica_rentabilidade(id_produto, nome_produto, preco, preco_unitario, erro):
    """Calcula, verifica e retorna a rentabilidade do item do pedido"""
    
    rentabilidade = "Rentabilidade "
    margem = Decimal(0.1) * preco_unitario
    preco_com_margem = preco_unitario - margem

    if(preco > preco_unitario):
        rentabilidade += "ótima"
    elif(preco >= preco_com_margem):
        rentabilidade += "boa"
    else:
        rentabilidade += "ruim"    
        if(erro):
            mensagem = 'O produto (cod={}:{}, preço:{}) possui {}. Melhore sua oferta ({}) se quiser este maravilhoso produto.'.format(
                id_produto,
                nome_produto,
                preco_unitario,
                rentabilidade,
                preco)
            raise ValidationError({'rentabilidade': mensagem})
    
    if not erro:
        return rentabilidade

    
