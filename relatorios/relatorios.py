# -*- coding: utf-8 -*-


class TotalCategoria():

    def __init__(self, categoria, valor):
        self.descricao = categoria
        self.valor = valor


class TotalEtapa():

    def __init__(self, etapa, valor):
        self.descricao = etapa
        self.valor = valor


class Clientes():

    def __init__(self):
        self.cliente = ''
        self.telefones = []
        self.obras = []
