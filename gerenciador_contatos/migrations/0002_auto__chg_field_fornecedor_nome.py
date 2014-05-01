# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Fornecedor.nome'
        db.alter_column(u'gerenciador_contatos_fornecedor', 'nome', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Fornecedor.nome'
        db.alter_column(u'gerenciador_contatos_fornecedor', 'nome', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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