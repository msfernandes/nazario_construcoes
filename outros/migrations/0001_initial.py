# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Etapa'
        db.create_table(u'outros_etapa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'outros', ['Etapa'])

        # Adding model 'Categoria'
        db.create_table(u'outros_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'outros', ['Categoria'])

        # Adding model 'Mes'
        db.create_table(u'outros_mes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'outros', ['Mes'])


    def backwards(self, orm):
        # Deleting model 'Etapa'
        db.delete_table(u'outros_etapa')

        # Deleting model 'Categoria'
        db.delete_table(u'outros_categoria')

        # Deleting model 'Mes'
        db.delete_table(u'outros_mes')


    models = {
        u'outros.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'outros.etapa': {
            'Meta': {'object_name': 'Etapa'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'outros.mes': {
            'Meta': {'object_name': 'Mes'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['outros']