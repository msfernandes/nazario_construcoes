from django.contrib import admin
from django import forms

from suit.widgets import SuitDateWidget

from models import *

# Register your models here.


class ObraAdmin(admin.ModelAdmin):
    fields = ('valor_contrato', 'data_inicio', 'data_fim',
              'endereco_obra', 'cliente', 'observacoes')

    list_display = ('cliente', 'endereco_obra', 'valor_contrato',
                    'data_inicio', 'data_fim', 'observacoes')

    #form = ObraForm
admin.site.register(Obra, ObraAdmin)


class VencimentoInline(admin.TabularInline):
    model = Boleto
    extra = 1


class DespesaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados da Despesa', {'fields': ['valor', 'data_compra',
                                         'tipo_despesa']}),
        ('Dados Adicionais', {'fields': ['obra', 'categoria',
                                         'fornecedor', 'etapa']})
    ]

    inlines = (VencimentoInline,)

    list_display = ('data_compra', 'valor', 'obra', 'categoria',
                    'fornecedor', 'etapa', 'tipo_despesa')
    list_filter = ['data_compra']
    date_hierarchy = 'data_compra'
admin.site.register(Despesa, DespesaAdmin)


class BoletoAdmin(admin.ModelAdmin):
    list_display = ('despesa', 'vencimento', 'valor',
                    'cod_barras', 'pago', 'conta')

    list_filter = ['pago', 'vencimento']
    date_hierarchy = 'vencimento'
admin.site.register(Boleto, BoletoAdmin)


class ReceitaForm(forms.ModelForm):

    class Meta:
        model = Receita
        widgets = {
            'data': SuitDateWidget,
        }


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('obra', 'data', 'valor')
    date_hierarchy = 'data'

    form = ReceitaForm
admin.site.register(Receita, ReceitaAdmin)
