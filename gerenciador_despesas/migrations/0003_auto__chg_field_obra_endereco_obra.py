# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Obra.endereco_obra'
        db.alter_column(u'gerenciador_despesas_obra', 'endereco_obra', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'Obra.endereco_obra'
        db.alter_column(u'gerenciador_despesas_obra', 'endereco_obra', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

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
        u'gerenciador_despesas.boleto': {
            'Meta': {'object_name': 'Boleto'},
            'cod_barras': ('django.db.models.fields.CharField', [], {'max_length': '170'}),
            'conta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gerenciador_contatos.Conta']", 'null': 'True', 'blank': 'True'}),
            'despesa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gerenciador_despesas.Despesa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pago': ('django.db.models.fields.BooleanField', [], {}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'vencimento': ('django.db.models.fields.DateField', [], {})
        },
        u'gerenciador_despesas.despesa': {
            'Meta': {'object_name': 'Despesa'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['outros.Categoria']"}),
            'data_compra': ('django.db.models.fields.DateField', [], {}),
            'etapa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['outros.Etapa']"}),
            'fornecedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gerenciador_contatos.Fornecedor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gerenciador_despesas.Obra']", 'null': 'True', 'blank': 'True'}),
            'tipo_despesa': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'})
        },
        u'gerenciador_despesas.obra': {
            'Meta': {'object_name': 'Obra'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gerenciador_contatos.Cliente']"}),
            'data_fim': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_inicio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'endereco_obra': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacoes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'valor_contrato': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'})
        },
        u'gerenciador_despesas.receita': {
            'Meta': {'object_name': 'Receita'},
            'data': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gerenciador_despesas.Obra']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'})
        },
        u'outros.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'outros.etapa': {
            'Meta': {'object_name': 'Etapa'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['gerenciador_despesas']