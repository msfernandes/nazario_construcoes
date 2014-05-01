# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(
        null=True,
        blank=True)

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __unicode__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    endereco = models.CharField(
        max_length=75,
        blank=True,
        verbose_name="Endereço"
    )

    def __unicode__(self):
        return self.nome


class TipoTelefone(models.Model):
    descricao = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Tipo do Telefone"
        verbose_name_plural = "Tipos de Telefone"

    def __unicode__(self):
        return self.descricao


class TelefoneCliente(models.Model):
    cliente = models.ForeignKey('Cliente')
    telefone = models.CharField(max_length=15)
    tag = models.ForeignKey('TipoTelefone', verbose_name="Tipo")

    class Meta:
        verbose_name = "Telefone de Cliente"
        verbose_name_plural = "Telefones de Clientes"


class TelefoneFornecedor(models.Model):
    fornecedor = models.ForeignKey('Fornecedor')
    telefone = models.CharField(max_length=15)
    tag = models.ForeignKey('TipoTelefone', verbose_name="Tipo")

    class Meta:
        verbose_name = "Telefone de Fornecedor"
        verbose_name_plural = "Telefones de Fornecedores"


class Conta(models.Model):
    banco = models.CharField(max_length=30)
    agencia = models.CharField(max_length=10)
    conta = models.CharField(max_length=15)
    titular = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s: %s/%s - %s' % (self.banco, self.agencia,
                                    self.conta, self.titular)
