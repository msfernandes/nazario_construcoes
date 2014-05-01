from django.contrib import admin
from django.forms import ModelForm

from suit.widgets import SuitDateWidget

from models import *

# Register your models here.


class TelefoneFornecedorInline(admin.TabularInline):
    model = TelefoneFornecedor
    extra = 1


class FornecedorAdmin(admin.ModelAdmin):
    inlines = [TelefoneFornecedorInline]
    fields = ('nome', 'email')

    list_display = ('nome', 'email')
admin.site.register(Fornecedor, FornecedorAdmin)


class TelefoneFornecedorAdmin(admin.ModelAdmin):
    list_display = ('fornecedor', 'telefone', 'tag')
admin.site.register(TelefoneFornecedor, TelefoneFornecedorAdmin)


class TelefoneClienteInline(admin.TabularInline):
    model = TelefoneCliente
    extra = 1


class ClienteAdmin(admin.ModelAdmin):
    inlines = [TelefoneClienteInline]
    fields = ['nome', 'email', 'endereco']

    list_display = ('nome', 'email', 'endereco')
admin.site.register(Cliente, ClienteAdmin)


class TelefoneClienteAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'telefone', 'tag')
admin.site.register(TelefoneCliente, TelefoneClienteAdmin)


class ContaAdmin(admin.ModelAdmin):
    list_display = ('conta', 'agencia', 'banco', 'titular')
admin.site.register(Conta, ContaAdmin)

admin.site.register(TipoTelefone)
