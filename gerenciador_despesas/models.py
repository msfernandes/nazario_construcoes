# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Obra(models.Model):
    valor_contrato = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Valor do Contrato"
    )

    data_inicio = models.DateField(
        blank=True,
        null=True,
        verbose_name="Início das Obras"
    )

    data_fim = models.DateField(
        blank=True,
        null=True,
        verbose_name="Final das Obras"
    )

    endereco_obra = models.CharField(
        max_length=255,
        verbose_name="Endereço"
    )

    cliente = models.ForeignKey('gerenciador_contatos.Cliente')
    observacoes = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.cliente, self.endereco_obra)


class Boleto(models.Model):
    despesa = models.ForeignKey('Despesa')
    valor = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="Valor da Parcela")

    vencimento = models.DateField()

    cod_barras = models.CharField(
        max_length=170,
        verbose_name="Código de Barras")

    pago = models.BooleanField()

    conta = models.ForeignKey('gerenciador_contatos.Conta',
                              blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def get_fornecedor(self):
        return self.despesa.fornecedor.nome
    get_fornecedor.short_description = 'Fornecedor'


TIPOS_DESPESA = (
    ('Obra', 'Obra'),
    ('Empresa', 'Empresa'),
    ('Pessoal', 'Pessoal')
)


class Despesa(models.Model):
    valor = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="Valor Total"
    )
    data_compra = models.DateField(
        verbose_name="Data de Compra")
    tipo_despesa = models.CharField(
        max_length=7,
        choices=TIPOS_DESPESA,
        verbose_name="Tipo")
    obra = models.ForeignKey('Obra', blank=True, null=True)
    categoria = models.ForeignKey('outros.Categoria')
    fornecedor = models.ForeignKey('gerenciador_contatos.Fornecedor')
    etapa = models.ForeignKey('outros.Etapa')

    def __unicode__(self):
        return u'(%s) %s - %s' % (self.data_compra, self.obra, self.categoria)


class Receita(models.Model):
    obra = models.ForeignKey('Obra')
    data = models.DateField()
    valor = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )
