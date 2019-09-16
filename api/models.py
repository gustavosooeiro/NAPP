from django.db import models
import datetime
from django.utils.html import format_html_join

from api.utils import formataPreco, formataReal, formataReal2

from collections import Counter

class Cliente(models.Model):
    def __str__(self):
        return self.nome
    nome = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']

class Produto(models.Model):
    def __str__(self):
        return self.nome + ", Preço unitário: " + str(self.preco_unitario)
    
    nome = models.CharField(max_length=200)
    preco_unitario = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    multiplo = models.IntegerField(blank=True, null=True)


def incrementa_id_pedido():
    prefix = 'StarWars-'  
    ultimo_pedido = Pedido.objects.all().order_by('id').last()
    if not ultimo_pedido:
        return str(prefix) + str(datetime.date.today().year) + str(
            datetime.date.today().month).zfill(2) + str(
            datetime.date.today().day).zfill(2) + '0001'
    pedido_id = ultimo_pedido.pedido_id
    pedido_id_int = int(pedido_id[17:21])
    novo_pedido_id_int = pedido_id_int + 1
    novo_pedido_id =  str(prefix) + str(str(datetime.date.today().year)) + str(
        datetime.date.today().month).zfill(2) + str(
        datetime.date.today().day).zfill(2) + str(novo_pedido_id_int).zfill(4)
    return novo_pedido_id

class Pedido(models.Model):
    
    NAOPAGO = 0
    PROCESSANDO = 1
    PAGO = 2
    
    STATUS_PAGAMENTO = (
        (NAOPAGO, 'Não Pago'),
        (PROCESSANDO, 'Processando pedido'),
        (PAGO, 'Pago'),
    )

    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, null=True, blank=True)
    pedido_id = models.CharField(max_length=30, default=incrementa_id_pedido, null=True, blank=True, editable=False)
    status_pagamento = models.IntegerField(default=NAOPAGO, choices=STATUS_PAGAMENTO, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.pedido_id)
    
    def total(self):
        itens = ItensPedido.objects.filter(pedido=self.pk)
        valor = sum(Counter(item.preco * item.quantidade for item in itens))
        return str(valor)

    def detalhes(self):
        itens = ItensPedido.objects.filter(pedido=self.pk)
        return format_html_join('\n', "{} ({} x {} = {})<br/>", 
                                ((item.produto.nome,str(item.quantidade),item.preco,str(item.preco * item.quantidade)) for item in itens))
    

class ItensPedido(models.Model):

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE,related_name='itemspedido', null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produtos', null=True)
    preco = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    quantidade = models.IntegerField(default=1, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pedido.pedido_id + ": " + self.produto.nome + ", preço: " + str(self.preco) + ", quantidade: " + str(self.quantidade)

    
