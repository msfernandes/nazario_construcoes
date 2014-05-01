# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Etapa(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"

    def __unicode__(self):
        return self.descricao


class Categoria(models.Model):
    descricao = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.descricao


class Mes(models.Model):
    descricao = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Mes'
        verbose_name_plural = 'Meses'

    def __unicode__(self):
        pass
