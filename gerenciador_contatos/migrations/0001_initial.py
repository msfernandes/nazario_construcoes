# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fornecedor'
        db.create_table(u'gerenciador_contatos_fornecedor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'gerenciador_contatos', ['Fornecedor'])

        # Adding model 'Cliente'
        db.create_table(u'gerenciador_contatos_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
        ))
        db.send_create_signal(u'gerenciador_contatos', ['Cliente'])

        # Adding model 'TipoTelefone'
        db.create_table(u'gerenciador_contatos_tipotelefone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'gerenciador_contatos', ['TipoTelefone'])

        # Adding model 'TelefoneCliente'
        db.create_table(u'gerenciador_contatos_telefonecliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gerenciador_contatos.Cliente'])),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gerenciador_contatos.TipoTelefone'])),
        ))
        db.send_create_signal(u'gerenciador_contatos', ['TelefoneCliente'])

        # Adding model 'TelefoneFornecedor'
        db.create_table(u'gerenciador_contatos_telefonefornecedor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fornecedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gerenciador_contatos.Fornecedor'])),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gerenciador_contatos.TipoTelefone'])),
        ))
        db.send_create_signal(u'gerenciador_contatos', ['TelefoneFornecedor'])

        # Adding model 'Conta'
        db.create_table(u'gerenciador_contatos_conta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('banco', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('agencia', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('conta', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('titular', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'gerenciador_contatos', ['Conta'])


    def backwards(self, orm):
        # Deleting model 'Fornecedor'
        db.delete_table(u'gerenciador_contatos_fornecedor')

        # Deleting model 'Cliente'
        db.delete_table(u'gerenciador_contatos_cliente')

        # Deleting model 'TipoTelefone'
        db.delete_table(u'gerenciador_contatos_tipotelefone')

        # Deleting model 'TelefoneCliente'
        db.delete_table(u'gerenciador_contatos_telefonecliente')

        # Deleting model 'TelefoneFornecedor'
        db.delete_table(u'gerenciador_contatos_telefonefornecedor')

        # Deleting model 'Conta'
        db.delete_table(u'gerenciador_contatos_conta')


    models = {
        u'gerenciador_contatos.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'gerenciador_contatos.conta': {
            'Meta': {'object_name': 'Conta'},
            'agencia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'banco': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'conta': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titular': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'gerenciador_contatos.fornecedor': {
            'Meta': {'object_name': 'Fornecedor'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gerenciador_contatos.telefonecliente': {
            'Meta': {'object_name': 'TelefoneCliente'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gerenciador_contatos.Cliente']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gerenciador_contatos.TipoTelefone']"}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'gerenciador_contatos.telefonefornecedor': {
            'Meta': {'object_name': 'TelefoneFornecedor'},
            'fornecedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gerenciador_contatos.Fornecedor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gerenciador_contatos.TipoTelefone']"}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'gerenciador_contatos.tipotelefone': {
            'Meta': {'object_name': 'TipoTelefone'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['gerenciador_contatos']